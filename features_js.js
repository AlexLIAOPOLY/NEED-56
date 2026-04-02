// ===== KEYBOARD NAVIGATION =====
document.addEventListener('keydown', e => {
  const key = parseInt(e.key);
  if(key >= 1 && key <= 8 && !e.ctrlKey && !e.metaKey && !e.altKey) {
    const navItems = document.querySelectorAll('.ni');
    if(navItems[key-1]) navItems[key-1].click();
  }
  // Escape closes notif panel
  if(e.key === 'Escape') {
    const p = document.getElementById('notif-panel');
    if(p) p.style.display = 'none';
  }
});

// ===== TICKER BAR =====
const TICKER_DATA = [
  {label:'CMHK (0762.HK)', val:6.82, chg:+0.04, pct:+0.59},
  {label:'USD/HKD', val:7.7821, chg:-0.0012, pct:-0.02},
  {label:'恒生指数', val:19842, chg:+234, pct:+1.19},
  {label:'10Y HKD Bond', val:3.82, chg:+0.03, pct:+0.79},
  {label:'WTI Crude', val:81.4, chg:-0.6, pct:-0.73},
  {label:'CSL (上市母公司)', val:18.24, chg:-0.18, pct:-0.98},
  {label:'通胀CPI(HK)', val:2.4, chg:+0.1, pct:null},
  {label:'Prime Rate', val:5.875, chg:0, pct:0},
];
function buildTicker() {
  const bar = document.getElementById('ticker-bar');
  if(!bar) return;
  const html = TICKER_DATA.map(t => {
    const sign = t.chg > 0 ? '+' : '';
    const color = t.chg > 0 ? 'var(--a3)' : t.chg < 0 ? 'var(--dn)' : 'var(--t3)';
    const pctStr = t.pct !== null ? ` (${t.pct > 0?'+':''}${t.pct}%)` : '';
    return `<span class="tick-item"><span class="tick-label">${t.label}</span><span class="tick-val" style="color:${color}">${t.val} ${sign}${t.chg}${pctStr}</span></span>`;
  }).join('<span class="tick-sep">|</span>');
  // Duplicate for seamless scroll
  bar.innerHTML = `<div class="tick-track">${html}${html}</div>`;
}
buildTicker();
// Randomize ticker slightly every 8s
setInterval(() => {
  TICKER_DATA.forEach(t => {
    const delta = (Math.random() - 0.5) * 0.01 * Math.abs(t.val);
    t.val = +( t.val + delta).toFixed(t.val > 100 ? 0 : t.val > 10 ? 2 : 3);
    t.chg = +(t.chg + (Math.random()-0.5)*0.02).toFixed(2);
  });
  buildTicker();
}, 8000);

// ===== GAUGE CHART (P0 health score) =====
function drawGauge(canvasId, value, max, color) {
  const canvas = document.getElementById(canvasId);
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  const cx = W/2, cy = H*0.72;
  const r = Math.min(W,H)*0.38;
  ctx.clearRect(0,0,W,H);
  // Background arc
  ctx.beginPath();
  ctx.arc(cx, cy, r, Math.PI, 2*Math.PI);
  ctx.strokeStyle = 'rgba(255,255,255,.08)';
  ctx.lineWidth = 14;
  ctx.stroke();
  // Value arc
  const pct = Math.min(value/max, 1);
  ctx.beginPath();
  ctx.arc(cx, cy, r, Math.PI, Math.PI + pct*Math.PI);
  ctx.strokeStyle = color;
  ctx.lineWidth = 14;
  ctx.lineCap = 'round';
  ctx.stroke();
  // Value text
  ctx.fillStyle = color;
  ctx.font = `bold ${Math.round(r*0.45)}px -apple-system`;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(value, cx, cy - r*0.1);
  // Label
  ctx.fillStyle = 'rgba(180,200,220,.6)';
  ctx.font = `${Math.round(r*0.2)}px -apple-system`;
  ctx.fillText('/ '+max, cx, cy + r*0.25);
}
setTimeout(() => {
  drawGauge('gauge-health', 78, 100, '#3b82f6');
  drawGauge('gauge-risk',   74, 100, '#f59e0b');
  drawGauge('gauge-nps',    62, 100, '#22c55e');
}, 300);

// ===== EXPORT REPORT =====
function exportReport() {
  const now = new Date().toLocaleString('zh-HK');
  const report = `CMHK 决策仿真系统 - 经营分析报告
生成时间: ${now}
${'='.repeat(50)}

【经营概览】
· 总用户数: 312.4万 (同比 +2.3%)
· 月度营收: 18.6亿HKD (同比 +4.1%)
· 综合ARPU: 198 HKD (同比 -1.2%)
· 净推荐值NPS: 62分 (季度 +5pts)
· 5G渗透率: 71.3% (目标75%)
· 客户流失率: 1.84% (预警阈值2.0%)
· 网络可用率: 99.96% (达标SLA)
· 经营利润率: 22.3% (目标24%)

【财务摘要】
· 年度营收: 221.8亿HKD (+3.8%)
· EBITDA: 74.2亿 (利润率33.5%)
· 资本开支: 28.4亿 (-6.1%)
· 自由现金流: 45.8亿 (+12.3%)

【风险评估】
· 综合风险评级: 中高
· 高风险项: 频谱重组(9.1), 用户流失(8.6)
· 中风险项: 价格战(7.2), 网络安全(6.8)

【市场格局】
· CMHK市占率: 28.4% (行业第一)
· 主要竞对: CSL 24.1%, SmarTone 21.8%, 3HK 19.3%

【预测结论】
· 12个月营收预测: +4.2% ~ +5.8% (五种算法均值)
· 预测用户净增: +8.2万
· 预测ARPU: 204 HKD

【战略建议】
1. 启动$158阻击套餐对抗3HK价格战
2. 提交OFCA频谱咨询回应(截止4月30日)
3. 加速企业专线B2B拓展, 目标新增200家
4. 推进5G SA独立组网升级
5. 大湾区跨境专线优先布局

--- 由 CMHK 决策仿真系统 自动生成 ---`;
  const blob = new Blob(['\uFEFF'+report], {type:'text/plain;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'CMHK_决策报告_'+new Date().toISOString().slice(0,10)+'.txt';
  a.click();
}
