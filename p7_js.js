// ===== P7 DATA INGESTION ENGINE =====
const DS_SOURCES = [
  {id:'r-bss',  name:'BSS',     cls:'row-fin', types:['套餐变更','账单生成','用户开户','流量超限'],   color:'#22c55e'},
  {id:'r-oss',  name:'OSS',     cls:'row-net', types:['5G告警','基站离线','流量峰值','时延超标'],   color:'#3b82f6'},
  {id:'r-crm',  name:'CRM',     cls:'row-mkt', types:['投诉工单','NPS反馈','客户流失风险','商机'],   color:'#fb923c'},
  {id:'r-erp',  name:'ERP',     cls:'row-fin', types:['收入确认','成本录入','EBITDA更新','Capex'], color:'#22c55e'},
  {id:'r-dpi',  name:'DPI',     cls:'row-net', types:['流量分类','应用识别','用户画像','异常流量'], color:'#3b82f6'},
  {id:'r-spider',name:'竞对',   cls:'row-mkt', types:['套餐更新','价格变动','新产品','促销活动'],   color:'#f59e0b'},
  {id:'r-news', name:'舆情',    cls:'row-risk', types:['负面报道','监管动态','行业新闻','社媒热点'], color:'#f43f5e'},
];

// Spark line data per source
const sparkData = {};
DS_SOURCES.forEach(s => { sparkData[s.id] = Array.from({length:8}, ()=>Math.random()*8+2); });

function renderSpark(id) {
  const el = document.getElementById(id);
  if(!el) return;
  const data = sparkData[id];
  const max = Math.max(...data);
  el.innerHTML = data.map(v =>
    `<div class="ds-spark-bar" style="height:${Math.round(v/max*16)}px"></div>`
  ).join('');
}

function updateSparks() {
  DS_SOURCES.forEach(s => {
    sparkData[s.id].shift();
    sparkData[s.id].push(Math.random()*10+1);
    renderSpark(s.id);
  });
}

// Initialize sparks
DS_SOURCES.forEach(s => renderSpark(s.id));

// Data stream rows
let pktTotal = 12840000;
const streamEl = document.getElementById('data-stream');
const eventEl = document.getElementById('event-feed');

function addStreamRow() {
  if(!streamEl) return;
  const src = DS_SOURCES[Math.floor(Math.random()*DS_SOURCES.length)];
  const type = src.types[Math.floor(Math.random()*src.types.length)];
  const now = new Date();
  const ts = now.toTimeString().slice(0,8);
  const vals = {
    'BSS': ()=>`用户ID:${Math.floor(Math.random()*9e6+1e6)} ARPU:$${(180+Math.random()*80).toFixed(0)}`,
    'OSS': ()=>`站点:${['HKI','KLN','NT','LT'][Math.floor(Math.random()*4)]}-${Math.floor(Math.random()*999)} 可用率:${(99.8+Math.random()*.2).toFixed(2)}%`,
    'CRM': ()=>`客户:${Math.floor(Math.random()*9e5+1e5)} 评分:${(60+Math.random()*40).toFixed(0)}`,
    'ERP': ()=>`科目:${['移动','固网','企业'][Math.floor(Math.random()*3)]} 金额:${(Math.random()*500+100).toFixed(1)}万`,
    'DPI': ()=>`协议:${['HTTP','5G-SA','VoLTE','IoT'][Math.floor(Math.random()*4)]} 流量:${(Math.random()*100).toFixed(1)}MB`,
    '竞对': ()=>`运营商:${['CSL','3HK','SmarTone'][Math.floor(Math.random()*3)]} 套餐:$${(120+Math.random()*150).toFixed(0)}`,
    '舆情': ()=>`来源:${['HKEJ','明报','微博','Twitter'][Math.floor(Math.random()*4)]} 情感:${Math.random()>.3?'中性':'负面'}`,
  };
  const valFn = vals[src.name] || (()=>'数据包已接收');
  const div = document.createElement('div');
  div.className = `ds-row ${src.cls}`;
  div.innerHTML = `<span class="ds-ts">${ts}</span><span class="ds-src">${src.name}</span><span class="ds-type"><span class="tag tb2">${type}</span></span><span class="ds-val">${valFn()}</span>`;
  streamEl.insertBefore(div, streamEl.firstChild);
  if(streamEl.children.length > 60) streamEl.removeChild(streamEl.lastChild);
  // update packet count
  pktTotal += Math.floor(Math.random()*500+100);
  const el = document.getElementById('pkt-count');
  if(el) el.textContent = (pktTotal/1e4).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  // update rate
  const rateEl = document.getElementById('stream-rate');
  if(rateEl) rateEl.textContent = `${(Math.random()*3+10).toFixed(1)}万条/s`;
  // update latency
  const latEl = document.getElementById('latency');
  if(latEl) latEl.textContent = (0.8+Math.random()*0.8).toFixed(1);
}

function addEventRow() {
  if(!eventEl) return;
  const events = [
    {cls:'row-fin', tag:'财务', msg:`ERP同步: Q${Math.ceil(Math.random()*4)}营收更新，差值 +${(Math.random()*0.5).toFixed(2)}亿`},
    {cls:'row-net', tag:'网络', msg:`OSS告警: ${['九龙','新界','香港岛'][Math.floor(Math.random()*3)]}区 5G时延 ${(3+Math.random()*3).toFixed(1)}ms`},
    {cls:'row-mkt', tag:'竞对', msg:`爬虫更新: ${['CSL','3HK','SmarTone'][Math.floor(Math.random()*3)]} 套餐价格变动`},
    {cls:'row-risk', tag:'舆情', msg:`监测到负面话题: CMHK 客服投诉 热度 ${Math.floor(Math.random()*50+10)}`},
    {cls:'row-fin', tag:'CRM', msg:`NPS反馈: 本周 ${Math.floor(Math.random()*200+800)} 份，均分 ${(58+Math.random()*8).toFixed(1)}`},
  ];
  const e = events[Math.floor(Math.random()*events.length)];
  const now = new Date().toTimeString().slice(0,8);
  const div = document.createElement('div');
  div.className = 'ds-item';
  div.innerHTML = `<div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">${e.msg}</div><div class="ds-meta">${now} · ${e.tag}</div></div>`;
  eventEl.insertBefore(div, eventEl.firstChild);
  if(eventEl.children.length > 8) eventEl.removeChild(eventEl.lastChild);
}

// Ingest volume chart
C('c-ingest',{type:'line',data:{
  labels:['00:00','02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00','now'],
  datasets:[
    {label:'内部数据(万条/min)',data:[82,76,70,68,95,142,168,175,180,165,158,145,152],borderColor:'#3b82f6',backgroundColor:'rgba(59,130,246,.06)',fill:true,tension:.4,pointRadius:2,borderWidth:1.5},
    {label:'外部数据(万条/min)',data:[12,10,9,8,15,28,32,35,38,30,28,22,25],borderColor:'#f59e0b',fill:false,tension:.4,pointRadius:2,borderWidth:1.5}
  ]
},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'top',labels:{boxWidth:10,padding:10}}},scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(26,36,54,.8)'},ticks:{callback:v=>v+'万'}}}}});

function retrySource(btn) {
  btn.textContent = '连接中...';
  btn.style.color = 'var(--wn)';
  setTimeout(()=>{
    btn.textContent = '已恢复';
    btn.style.color = 'var(--a3)';
    const dot = btn.closest('.ds-item').querySelector('.ds-dot');
    if(dot){dot.className='ds-dot ds-live';}
    const tag = btn.previousElementSibling;
    if(tag){tag.className='tag tg';tag.textContent='正常';}
  }, 2000);
}

// Start live simulation
setInterval(addStreamRow, 600);
setInterval(addEventRow, 3500);
setInterval(updateSparks, 1200);
// Init with some rows
for(let i=0;i<12;i++) addStreamRow();
for(let i=0;i<5;i++) addEventRow();
