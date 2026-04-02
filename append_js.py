js = """
<script>
const PAGE_TITLES=['决策总览','财务分析','运营监控','市场洞察','风险研判','场景模拟','行业趋势'];
const PAGE_SUBS=['实时经营数据 · 内外部环境整合分析','收入 · 成本 · 利润 · 现金流全景','网络质量 · 用户增长 · 服务水平','竞对动态 · 政策监管 · 行业趋势','风险识别 · 量化评估 · 应对策略','参数仿真 · 蒙特卡洛预测 · 决策优化','全球电信 · 技术趋势 · 战略机遇'];
function goPage(el,idx){document.querySelectorAll('.ni').forEach(n=>n.classList.remove('act'));el.classList.add('act');document.querySelectorAll('.page').forEach(p=>p.classList.remove('act'));document.getElementById('p'+idx).classList.add('act');document.getElementById('tb-title').textContent=PAGE_TITLES[idx];document.getElementById('tb-sub').textContent=PAGE_SUBS[idx];}
function tick(){const ts=new Date().toLocaleTimeString('zh-HK',{hour12:false});document.getElementById('tb-time').textContent=ts;document.getElementById('sf-time').textContent='最后同步 '+ts;}
setInterval(tick,1000);tick();
function syncData(){const btn=document.getElementById('sync-btn');btn.textContent='同步中...';btn.classList.add('loading');setTimeout(()=>{btn.textContent='同步数据';btn.classList.remove('loading');tick();},1400);}
let currentRange='3M';
function setRange(el,range){document.querySelectorAll('.fb-btn').forEach(b=>b.classList.remove('act'));el.classList.add('act');currentRange=range;refreshRevChart();}
function exportCSV(){const rows=[['业务线','营收(亿HKD)','同比变化','毛利率','净利润(亿)','收入贡献'],['移动通信','150.6','+4.2%','48.3%','28.6','67.9%'],['固网宽带','32.4','+2.1%','41.7%','6.8','14.6%'],['企业专线','24.8','+8.6%','55.2%','7.2','11.2%'],['国际漫游','8.6','-3.4%','38.1%','1.2','3.9%'],['数字服务','5.4','+22.3%','62.8%','1.8','2.4%']];const csv=rows.map(r=>r.join(',')).join('\n');const blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='CMHK_财务数据_'+new Date().toISOString().slice(0,10)+'.csv';a.click();}
Chart.defaults.color='#4e6a8a';Chart.defaults.borderColor='#1a2436';
Chart.defaults.font.family="-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif";
Chart.defaults.font.size=10.5;
const RDATA={'1M':{labels:['W1','W2','W3','W4'],rev:[18.1,18.3,18.5,18.6],tgt:[18.2,18.4,18.6,18.8]},'3M':{labels:['1\u6708','2\u6708','3\u6708'],rev:[17.9,18.3,18.6],tgt:[18.1,18.4,19.0]},'6M':{labels:['10\u6708','11\u6708','12\u6708','1\u6708','2\u6708','3\u6708'],rev:[17.2,17.5,17.8,17.9,18.3,18.6],tgt:[17.4,17.6,18.0,18.1,18.4,19.0]},'1Y':{labels:['4\u6708','5\u6708','6\u6708','7\u6708','8\u6708','9\u6708','10\u6708','11\u6708','12\u6708','1\u6708','2\u6708','3\u6708'],rev:[16.2,16.8,17.1,17.4,17.0,17.8,18.0,18.2,17.9,18.3,18.5,18.6],tgt:[16.5,17.0,17.2,17.5,17.5,17.8,18.2,18.4,18.2,18.5,18.8,19.0]},'YTD':{labels:['1\u6708','2\u6708','3\u6708'],rev:[17.9,18.3,18.6],tgt:[18.1,18.4,19.0]}};
const charts={};
const C=(id,cfg)=>{charts[id]=new Chart(id,cfg);return charts[id];};
const gridColor='rgba(26,36,54,.8)';
const opt=(extra={})=>(Object.assign({responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}}},extra));

charts['c-rev-chart']=C('c-rev-chart',{type:'line',data:{labels:RDATA['3M'].labels,datasets:[{label:'\u8425\u6536',data:RDATA['3M'].rev,borderColor:'#3b82f6',backgroundColor:'rgba(59,130,246,.06)',fill:true,tension:.4,pointRadius:3,pointHoverRadius:5,borderWidth:1.5},{label:'\u76ee\u6807',data:RDATA['3M'].tgt,borderColor:'#3d5470',borderDash:[4,3],fill:false,tension:.4,pointRadius:0,borderWidth:1.5}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'top',labels:{boxWidth:10,padding:12}}},scales:{x:{grid:{display:false}},y:{grid:{color:gridColor},ticks:{callback:v=>v+'\u4ebf'}}}}});

function refreshRevChart(){const d=RDATA[currentRange];const ch=charts['c-rev-chart'];ch.data.labels=d.labels;ch.data.datasets[0].data=d.rev;ch.data.datasets[1].data=d.tgt;ch.update();}

C('c-biz',{type:'doughnut',data:{labels:['\u79fb\u52a8\u901a\u4fe1','\u56fa\u7f51\u5bbd\u5e26','\u4f01\u4e1a\u4e13\u7ebf','\u56fd\u9645\u6f2b\u6e38','\u6570\u5b57\u670d\u52a1'],datasets:[{data:[67.9,14.6,11.2,3.9,2.4],backgroundColor:['#3b82f6','#22d3ee','#22c55e','#f59e0b','#818cf8'],borderWidth:0,hoverOffset:5}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'right',labels:{boxWidth:10,padding:8,font:{size:10}}}}}});
C('c-usr',{type:'bar',data:{labels:['\u4e2a\u4eba','\u4f01\u4e1a','\u5bb6\u5ead\u5bbd\u5e26','\u7269\u8054\u7f51'],datasets:[{data:[198.4,62.3,41.2,10.5],backgroundColor:['#3b82f6','#22c55e','#22d3ee','#818cf8'],borderRadius:4,borderSkipped:false}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{grid:{color:gridColor},ticks:{callback:v=>v+'\u4e07'}}}}});
"""

with open('/Users/liaowang/Desktop/需求56/index.html', 'a', encoding='utf-8') as f:
    f.write(js)
print('JS part 1 appended, lines:', open('/Users/liaowang/Desktop/需求56/index.html').read().count('\n'))
