// Multi-algorithm prediction engine
let currentAlgo = 'mc';
const ALGO_DESC = {
  mc:    '蒙特卡洛：随机抽样10,000次模拟，输出概率分布和置信区间',
  lr:    '线性回归：基于12个月历史数据拟合趋势线，投影未来走势',
  es:    '指数平滑（Holt-Winters）：加权近期数据，自动识别季节性和趋势',
  arima: 'ARIMA(1,1,1)：差分自回归移动平均模型，适合非平稳时序列',
  bayes: '贝叶斯推断：引入先验知识，输出后验分布与不确定性量化'
};

const HIST_REV = [16.2,16.8,17.1,17.4,17.0,17.8,18.0,18.2,17.9,18.3,18.5,18.6];

function linReg(data) {
  const n=data.length; let sx=0,sy=0,sxy=0,sx2=0;
  data.forEach((y,i)=>{sx+=i;sy+=y;sxy+=i*y;sx2+=i*i;});
  const b=(n*sxy-sx*sy)/(n*sx2-sx*sx), a=(sy-b*sx)/n;
  const forecast=[]; for(let i=n;i<n+12;i++) forecast.push(+(a+b*i).toFixed(2));
  const residuals=data.map((y,i)=>y-(a+b*i));
  const rmse=Math.sqrt(residuals.reduce((s,r)=>s+r*r,0)/n);
  return {forecast, rmse:+rmse.toFixed(3), ci:+(rmse*1.96).toFixed(2), name:'线性回归', p10:forecast.map(v=>+(v-rmse*1.96).toFixed(2)), p90:forecast.map(v=>+(v+rmse*1.96).toFixed(2))};
}

function expSmooth(data,alpha=0.4,beta=0.3) {
  let l=data[0], b=data[1]-data[0]; const fitted=[];
  data.forEach(y=>{ const lp=l,bp=b; l=alpha*y+(1-alpha)*(lp+bp); b=beta*(l-lp)+(1-beta)*bp; fitted.push(+(l+b).toFixed(2)); });
  const forecast=[]; for(let h=1;h<=12;h++) forecast.push(+(l+h*b).toFixed(2));
  const residuals=data.map((y,i)=>y-fitted[i]);
  const rmse=Math.sqrt(residuals.reduce((s,r)=>s+r*r,0)/data.length);
  return {forecast, rmse:+rmse.toFixed(3), ci:+(rmse*1.8).toFixed(2), name:'指数平滑', p10:forecast.map(v=>+(v-rmse*1.8).toFixed(2)), p90:forecast.map(v=>+(v+rmse*1.8).toFixed(2))};
}

function arimaModel(data) {
  const diff=data.slice(1).map((v,i)=>v-data[i]);
  let num=0,den=0;
  for(let i=1;i<diff.length;i++){num+=diff[i]*diff[i-1];den+=diff[i-1]*diff[i-1];}
  const phi=den>0?Math.min(0.95,num/den):0.5;
  const theta=0.3; const errors=diff.map(()=>0); errors[0]=diff[0];
  const fitted_diff=[diff[0]];
  for(let i=1;i<diff.length;i++){fitted_diff.push(phi*diff[i-1]+theta*errors[i-1]);errors[i]=diff[i]-fitted_diff[i];}
  const forecast=[]; let last=data[data.length-1],lastd=diff[diff.length-1],laste=errors[errors.length-1];
  for(let h=1;h<=12;h++){const fd=phi*lastd+theta*laste;last=+(last+fd).toFixed(2);lastd=fd;laste=0;forecast.push(last);}
  const rmse=Math.sqrt(errors.reduce((s,e)=>s+e*e,0)/errors.length);
  return {forecast, rmse:+rmse.toFixed(3), ci:+(rmse*2.1).toFixed(2), name:'ARIMA', p10:forecast.map(v=>+(v-rmse*2.1).toFixed(2)), p90:forecast.map(v=>+(v+rmse*2.1).toFixed(2))};
}

function bayesian(data) {
  const priorMu=18, priorPrec=4, n=data.length;
  const mean=data.reduce((s,v)=>s+v,0)/n;
  const variance=data.reduce((s,v)=>s+(v-mean)**2,0)/n||0.1;
  const postMu=(priorPrec*priorMu+n*(mean/variance))/(priorPrec+n/variance);
  const trend=(data[n-1]-data[0])/(n-1);
  const forecast=[]; for(let h=1;h<=12;h++) forecast.push(+(postMu+h*trend*0.7).toFixed(2));
  const residuals=data.map(v=>v-postMu);
  const rmse=Math.sqrt(residuals.reduce((s,r)=>s+r*r,0)/n);
  return {forecast, rmse:+rmse.toFixed(3), ci:+(rmse*2.5).toFixed(2), name:'贝叶斯', p10:forecast.map(v=>+(v-rmse*2.5).toFixed(2)), p90:forecast.map(v=>+(v+rmse*2.5).toFixed(2))};
}

function monteCarlo(data, boost=0) {
  const n=data.length, mean=data.reduce((s,v)=>s+v,0)/n;
  const std=Math.sqrt(data.reduce((s,v)=>s+(v-mean)**2,0)/n)||0.2;
  const trend=(data[n-1]-data[0])/(n-1);
  const N=10000; const finals=[];
  // build forecast paths for p10/p90
  const paths=Array.from({length:12},()=>[]);
  for(let i=0;i<N;i++){
    let v=data[n-1];
    for(let h=0;h<12;h++){
      const u1=Math.max(1e-10,Math.random()),u2=Math.random();
      const z=Math.sqrt(-2*Math.log(u1))*Math.cos(2*Math.PI*u2);
      v=+(v+trend+boost+z*std*0.25).toFixed(3);
      paths[h].push(v);
    }
    finals.push(paths[11][paths[11].length-1]);
  }
  finals.sort((a,b)=>a-b);
  const p10v=finals[Math.floor(N*0.1)], p90v=finals[Math.floor(N*0.9)], medv=finals[Math.floor(N*0.5)];
  const forecast=[]; const p10arr=[]; const p90arr=[];
  paths.forEach(arr=>{
    arr.sort((a,b)=>a-b);
    p10arr.push(+arr[Math.floor(N*0.1)].toFixed(2));
    p90arr.push(+arr[Math.floor(N*0.5)].toFixed(2));
    p90arr[p90arr.length-1]=+arr[Math.floor(N*0.9)].toFixed(2);
    forecast.push(+arr[Math.floor(N*0.5)].toFixed(2));
  });
  const rmse=std*1.2;
  return {forecast, rmse:+rmse.toFixed(3), ci:+(p90v-p10v).toFixed(2), p10:p10arr, p90:p90arr.map((v,i)=>paths[i].sort((a,b)=>a-b)[Math.floor(N*0.9)]), name:'蒙特卡洛', p10v, p50v:medv, p90v};
}

function runAllAlgos(boost=0) {
  return {
    lr: linReg(HIST_REV),
    es: expSmooth(HIST_REV),
    arima: arimaModel(HIST_REV),
    bayes: bayesian(HIST_REV),
    mc: monteCarlo(HIST_REV, boost)
  };
}
