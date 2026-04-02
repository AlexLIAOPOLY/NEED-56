js = """
// Scenario engine
function updateScenario(){
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
  const pe=(price-198)/198*0.6,me=(mkt-85)/85*0.3,be=(b2b-1200)/1200*0.4;
  const revG=3.8+pe*100+me*100+be*100;
  const usrG=6.8+(mkt-85)/85*4+(fg-75)/75*6-(price-198)/198*8;
  const arpuP=Math.round(price*0.92+15);
  const profC=(-pe*50+(capex<28?(28-capex)*0.1:-(capex-28)*0.05)+be*30);
  const churnP=Math.max(0.8,1.84-churn/100*0.8);
  const npsP=Math.round((churn/100)*10+be*10+me*5);
  runMC(()=>{
    const setKPI=(id,val,sfx,isPos)=>{
      const el=document.getElementById(id);
      el.textContent=(isPos&&val>0?'+':'')+val.toFixed(1)+sfx;
      el.className='sc-kv '+(isPos?(val>=0?'pos':'neg'):'');
    };
    setKPI('sc-rev',revG,'%',true);
    document.getElementById('sc-usr').textContent=(usrG>=0?'+':'')+usrG.toFixed(1)+'\u4e07';
    document.getElementById('sc-usr').className='sc-kv '+(usrG>=0?'pos':'neg');
    document.getElementById('sc-arpu').textContent=arpuP;
    document.getElementById('sc-arpu').className='sc-kv';
    setKPI('sc-profit',profC,'pts',true);
    document.getElementById('sc-churn').textContent=churnP.toFixed(2)+'%';
    document.getElementById('sc-churn').className='sc-kv';
    document.getElementById('sc-nps').textContent='+'+ npsP+'pts';
    document.getElementById('sc-nps').className='sc-kv pos';
    // update radar
    scChart.data.datasets[1].data=[
      Math.min(100,55+revG*2),
      Math.min(100,60+usrG*1.5),
      Math.min(100,70+profC*3),
      Math.min(100,80+(fg-75)*0.5),
      Math.min(100,75+npsP*0.8),
      Math.min(100,65+be*20)
    ];
    scChart.update();
  });
}
function runMC(cb){
  const fill=document.getElementById('mc-fill');
  const status=document.getElementById('mc-status');
  status.textContent='Monte Carlo \u6a21\u62df\u4e2d\u2026';
  let p=0;
  const t=setInterval(()=>{
    p+=Math.random()*12+8;
    if(p>=100){p=100;clearInterval(t);setTimeout(()=>{fill.style.width='0%';status.textContent='Monte Carlo \u6a21\u62df\uff1a\u5c31\u7eea';cb();},200);}
    fill.style.width=Math.min(100,p)+'%';
  },50);
}
function resetScenario(){
  ['s-price','s-mkt','s-capex','s-b2b','s-5g','s-churn'].forEach(id=>{
    const defaults={s_price:198,s_mkt:85,s_capex:28,s_b2b:1200,'s-5g':75,'s-churn':50};
    document.getElementById(id).value=({s_price:198,'s-mkt':85,'s-capex':28,'s-b2b':1200,'s-5g':75,'s-churn':50})[id]||50;
  });
  document.getElementById('s-price').value=198;
  document.getElementById('s-mkt').value=85;
  document.getElementById('s-capex').value=28;
  document.getElementById('s-b2b').value=1200;
  document.getElementById('s-5g').value=75;
  document.getElementById('s-churn').value=50;
  updateScenario();
}

// Alert stream
const alerts=[
  {t:'\u9ad8',c:'#f43f5e',msg:'\u5ba2\u6237\u6d41\u5931\u7387\u8d8b\u8fd1\u9884\u8b661.84%\u9608\u503c'},
  {t:'\u4e2d',c:'#fb923c',msg:'3HK\u4ef7\u683c\u7b56\u7565\u5f71\u54cd\u4e2d\u4f4e\u7aef\u5e02\u573a'},
  {t:'\u4f4e',c:'#3b82f6',msg:'\u4f01\u4e1a\u5ba2\u6237\u7eed\u7b7e\u7387\u4e0b\u6ed187%\uff0c\u5173\u6ce8'},
  {t:'\u9ad8',c:'#f43f5e',msg:'OFCA\u9891\u8c31\u548b\u8be2\u622a\u62d64\u670830\u65e5'},
  {t:'\u4f4e',c:'#22c55e',msg:'5G\u5efa\u8bbe\u6295\u8d44\u8fdb\u5ea6\u6309\u8ba1\u5212\u63a8\u8fdb'},
];
const stream=document.getElementById('alert-stream');
alerts.forEach((a,i)=>{
  const d=document.createElement('div');
  d.className='stream-item';
  d.innerHTML=`<div class="stream-dot" style="background:${a.c}"></div><div><div class="stream-text">${a.msg}</div><div class="stream-time">${i===0?'\u521a\u521a':i+'\u5206\u949f\u524d'}</div></div>`;
  stream.appendChild(d);
});

updateScenario();
</script>
</body>
</html>
"""
with open('/Users/liaowang/Desktop/需求56/index.html', 'a', encoding='utf-8') as f:
    f.write(js)
content = open('/Users/liaowang/Desktop/需求56/index.html').read()
print('Done! lines:', content.count('\n'), 'has </html>:', '</html>' in content)
