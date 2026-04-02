function setAlgo(el, algo) {
  currentAlgo = algo;
  document.querySelectorAll('.algo-btn').forEach(b=>b.classList.remove('act'));
  el.classList.add('act');
  document.getElementById('algo-desc').textContent = ALGO_DESC[algo];
  updateScenario();
}

function updateScenario() {
  const price=+document.getElementById('s-price').value;
  const mkt=+document.getElementById('s-mkt').value;
  const capex=+document.getElementById('s-capex').value;
  const b2b=+document.getElementById('s-b2b').value;
  const fg=+document.getElementById('s-5g').value;
  const churn=+document.getElementById('s-churn').value;
  document.getElementById('v-price').textContent=price;
  document.getElementById('v-mkt').textContent=mkt;
  document.getElementById('v-capex').textContent=capex;
  document.getElementById('v-b2b').textContent=b2b;
  document.getElementById('v-5g').textContent=fg;
  document.getElementById('v-churn').textContent=churn;

  const pe=(price-198)/198, me=(mkt-85)/85, be=(b2b-1200)/1200;
  const boost = (-pe*0.15 + me*0.08 + be*0.06 + (fg-75)/75*0.04 + churn/100*0.03);
  const revG = +(3.8 + pe*(-8) + me*5 + be*4 + (fg-75)/75*2 + churn/100*1.5).toFixed(2);
  const usrG = +(6.8 + me*4 + (fg-75)/75*6 - pe*8 + churn/100*2).toFixed(1);
  const arpuP = Math.round(price*0.88 + 22);
  const profC = +(-pe*4 + (capex<28?(28-capex)*0.08:-(capex-28)*0.06) + be*2.5).toFixed(1);
  const churnP = +Math.max(0.6, 1.84 - churn/100*0.9).toFixed(2);
  const npsP = Math.round(churn/100*10 + be*8 + me*5);

  const status = document.getElementById('mc-status');
  const fill = document.getElementById('mc-fill');
  status.textContent = '计算中...';
  fill.style.width = '0%';

  let p=0;
  const anim = setInterval(()=>{
    p += Math.random()*15+10;
    if(p>=100){p=100;clearInterval(anim);}
    fill.style.width = Math.min(100,p)+'%';
  },30);

  setTimeout(()=>{
    clearInterval(anim);
    fill.style.width='100%';
    setTimeout(()=>{
      fill.style.width='0%';
      const all = runAllAlgos(boost);
      const cur = all[currentAlgo];
      status.textContent = '算法: '+cur.name+' | RMSE: '+cur.rmse+'亿';

      // Update RMSE display
      document.getElementById('algo-rmse').textContent = 'RMSE: '+cur.rmse+'亿';

      // KPI update
      const setKPI=(id,val,sfx,isPos)=>{
        const el=document.getElementById(id);
        el.textContent=(isPos&&val>0?'+':'')+val.toFixed(1)+sfx;
        el.className='sc-kv '+(isPos?(val>=0?'pos':'neg'):'');
      };
      setKPI('sc-rev',revG,'%',true);
      const uel=document.getElementById('sc-usr');
      uel.textContent=(usrG>=0?'+':'')+usrG+'万';
      uel.className='sc-kv '+(usrG>=0?'pos':'neg');
      document.getElementById('sc-arpu').textContent=arpuP;
      document.getElementById('sc-arpu').className='sc-kv';
      setKPI('sc-profit',profC,'pts',true);
      document.getElementById('sc-churn').textContent=churnP+'%';
      document.getElementById('sc-churn').className='sc-kv '+(churnP<1.84?'pos':'neg');
      document.getElementById('sc-nps').textContent='+'+(npsP>0?npsP:0)+'pts';
      document.getElementById('sc-nps').className='sc-kv pos';

      // CI display
      const lastF = cur.forecast[cur.forecast.length-1];
      const ciLow = +(lastF - cur.ci).toFixed(1);
      const ciHigh = +(lastF + cur.ci).toFixed(1);
      document.getElementById('ci-val').textContent = ciLow+'亿 ~ '+ciHigh+'亿';

      // Update radar
      scChart.data.datasets[1].data=[
        Math.min(100,55+revG*2.5),
        Math.min(100,60+usrG*1.5),
        Math.min(100,70+profC*4),
        Math.min(100,80+(fg-75)*0.6),
        Math.min(100,75+npsP),
        Math.min(100,65+be*25)
      ];
      scChart.update();

      // Update forecast chart with confidence band
      updateForecastChart(cur);

      // Update algo compare chart
      updateAlgoCompare(all);
    },150);
  }, currentAlgo==='mc'?800:300);
}

function updateForecastChart(res) {
  const labels = ['3月','4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','2月','3月'];
  const histLabels = ['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','2月','3月'];
  if(charts['c-forecast']) charts['c-forecast'].destroy();
  charts['c-forecast'] = new Chart('c-forecast',{
    type:'line',
    data:{
      labels:[...histLabels,...labels.slice(1)],
      datasets:[
        {label:'历史',data:[...HIST_REV,...Array(12).fill(null)],borderColor:'#7e96b4',fill:false,tension:.4,pointRadius:2,borderWidth:1.5,borderDash:[3,2]},
        {label:res.name+' 预测',data:[...Array(12).fill(null),HIST_REV[11],...res.forecast],borderColor:'#3b82f6',fill:false,tension:.4,pointRadius:3,borderWidth:2},
        {label:'P90',data:[...Array(13).fill(null),...res.p90],borderColor:'rgba(59,130,246,.2)',backgroundColor:'rgba(59,130,246,.08)',fill:'-1',tension:.4,pointRadius:0,borderWidth:0},
        {label:'P10',data:[...Array(13).fill(null),...res.p10],borderColor:'rgba(59,130,246,.2)',backgroundColor:'rgba(59,130,246,.08)',fill:false,tension:.4,pointRadius:0,borderWidth:0}
      ]
    },
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{position:'top',labels:{boxWidth:10,padding:10}}},
      scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(26,36,54,.8)'},ticks:{callback:v=>v+'亿'}}}}
  });
}

function updateAlgoCompare(all) {
  const algos = ['lr','es','arima','bayes','mc'];
  const names = algos.map(k=>all[k].name);
  const finalVals = algos.map(k=>all[k].forecast[11]);
  const ciVals = algos.map(k=>all[k].ci);
  const colors = ['#3b82f6','#22c55e','#f59e0b','#818cf8','#f43f5e'];
  if(charts['c-algo-compare']) charts['c-algo-compare'].destroy();
  charts['c-algo-compare'] = new Chart('c-algo-compare',{
    type:'bar',
    data:{
      labels:names,
      datasets:[
        {label:'12月预测营收',data:finalVals,backgroundColor:colors.map(c=>c+'bb'),borderRadius:5},
        {label:'置信区间(±)',data:ciVals,backgroundColor:colors.map(c=>c+'44'),borderRadius:5}
      ]
    },
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{position:'top',labels:{boxWidth:10,padding:10}}},
      scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(26,36,54,.8)'},ticks:{callback:v=>v+'亿'}}}}
  });
}

function resetScenario() {
  document.getElementById('s-price').value=198;
  document.getElementById('s-mkt').value=85;
  document.getElementById('s-capex').value=28;
  document.getElementById('s-b2b').value=1200;
  document.getElementById('s-5g').value=75;
  document.getElementById('s-churn').value=50;
  updateScenario();
}
