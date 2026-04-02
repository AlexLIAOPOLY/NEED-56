// ===== KPI COUNTER ANIMATION =====
const KPI_TARGETS = [
  {id:'v-users', from:305.0, to:312.4, dec:1, sfx:'<span class="ku">万</span>'},
  {id:'v-rev',   from:17.8,  to:18.6,  dec:1, sfx:'<span class="ku">亿HKD</span>'},
  {id:'v-arpu',  from:202,   to:198,   dec:0, sfx:'<span class="ku">HKD</span>'},
  {id:'v-nps',   from:57,    to:62,    dec:0, sfx:'<span class="ku">分</span>'},
  {id:'v-churnr',from:1.64,  to:1.84,  dec:2, sfx:'<span class="ku">%</span>'},
  {id:'v-margin',from:21.2,  to:22.3,  dec:1, sfx:'<span class="ku">%</span>'}
];
function animateAllKPIs() {
  KPI_TARGETS.forEach(k => {
    const el = document.getElementById(k.id);
    if(!el) return;
    const start = performance.now();
    const dur = 900;
    function step(now) {
      const p = Math.min((now-start)/dur, 1);
      const ease = 1 - Math.pow(1-p, 3);
      const val = k.from + (k.to - k.from) * ease;
      el.innerHTML = val.toFixed(k.dec) + k.sfx;
      el.classList.add('kv-flash');
      if(p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
}
setTimeout(animateAllKPIs, 500);

// ===== AI INSIGHT REFRESH =====
const AI_SETS = [
  [
    {cls:'ai-good',   label:'优势', text:'5G渗透率 71.3% 领先市场 3.4pts，企业专线增速 +8.6% 为各业务线最高，NPS 连续两季改善。'},
    {cls:'ai-warn',   label:'风险', text:'流失率上升趋势需本季度内遏止；3HK $138 套餐直接冲击 CMHK 中低端用户群，建议 48 小时内完成定价应对方案。'},
    {cls:'ai-info',   label:'机遇', text:'大湾区互通协议开启跨境专线新市场；AI 边缘计算需求爆发，建议优先布局深港双节点 MEC。'},
    {cls:'ai-action', label:'行动', text:'①启动 $158 阻击套餐审批 ②提交 OFCA 频谱咨询回应 ③召开企业客户续签专项会议。'}
  ],
  [
    {cls:'ai-good',   label:'财务', text:'Q1 EBITDA 利润率 33.5%，自由现金流增长 12.3%，资本开支下降 6.1% 显示投资效率提升。'},
    {cls:'ai-warn',   label:'成本', text:'ARPU 连续 3 季度下行，数据服务低价竞争压制单卡收益，需加快增值服务渗透进度。'},
    {cls:'ai-info',   label:'预测', text:'基于当前参数，五种算法均预测 Q2 营收正向增长，中位数预测 +4.2%。'},
    {cls:'ai-action', label:'行动', text:'①推动家庭宽带融合套餐提升 ARPU ②加速数字服务 API 开放 ③导入 AI 智能客服降低工单成本。'}
  ],
  [
    {cls:'ai-good',   label:'网络', text:'网络可用率 99.96% 达标 SLA，5G 小区数 8,642 个，平均下载速率 387 Mbps 行业领先。'},
    {cls:'ai-warn',   label:'运维', text:'月度投诉工单 1,248 件同比增 3.2%，首次解决率 78.3% 低于目标，需加强一线培训。'},
    {cls:'ai-info',   label:'机遇', text:'离岛 5G 覆盖仅 72%，提升至 85% 预计可带动 1.2 万新增用户和 ARPU 提升 $8。'},
    {cls:'ai-action', label:'行动', text:'①优先完成大屿山及离岛 5G 站址建设 ②优化工单分配系统 ③推进 5G SA 独立组网升级。'}
  ]
];
let aiIdx = 0;
function refreshAI() {
  aiIdx = (aiIdx + 1) % AI_SETS.length;
  const body = document.getElementById('ai-body');
  if(!body) return;
  body.style.opacity = '0';
  setTimeout(() => {
    body.innerHTML = AI_SETS[aiIdx].map(item =>
      `<div class="ai-item ${item.cls}"><span class="ai-label">${item.label}</span><span>${item.text}</span></div>`
    ).join('');
    body.style.opacity = '1';
    body.style.transition = 'opacity .3s';
  }, 200);
}
