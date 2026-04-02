content = open('/Users/liaowang/Desktop/需求56/index.html', encoding='utf-8').read()

# 1. Add ticker bar after topbar
old_filter = '  <div class="filter-bar">'
new_filter = '''  <div class="ticker-bar" id="ticker-bar"></div>
  <div class="filter-bar">'''
content = content.replace(old_filter, new_filter, 1)
print('ticker: OK' if 'ticker-bar' in content else 'ticker: FAIL')

# 2. Add export report button to filter bar
old_export = '<button class="fb-export" onclick="exportCSV()">导出 CSV</button>'
new_export = '<button class="fb-export" onclick="exportCSV()">导出 CSV</button><button class="fb-export" onclick="exportReport()" style="border-color:var(--pu);color:var(--pu)">导出报告</button>'
content = content.replace(old_export, new_export)
print('export btn: OK' if 'exportReport' in content else 'export btn: FAIL')

# 3. Add gauge cards to P0 - after the second g4 row (before g32)
old_g32 = '  <div class="g32">'
new_g32 = '''  <div class="g3" style="margin-bottom:12px">
    <div class="card"><div class="ch"><span class="ct">经营健康度</span></div><div style="display:flex;justify-content:space-around;align-items:center;padding:4px 0"><div style="text-align:center"><canvas id="gauge-health" width="110" height="70"></canvas><div style="font-size:9px;color:var(--t3);margin-top:2px">综合健康</div></div><div style="text-align:center"><canvas id="gauge-risk" width="110" height="70"></canvas><div style="font-size:9px;color:var(--t3);margin-top:2px">抗风险力</div></div><div style="text-align:center"><canvas id="gauge-nps" width="110" height="70"></canvas><div style="font-size:9px;color:var(--t3);margin-top:2px">客户口碑</div></div></div></div>
    <div class="card cs2"><div class="ch"><span class="ct">关键里程碑 / 战略进度</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
        <div class="br"><span class="bl">5G覆盖目标</span><div class="bt"><div class="bf" style="width:71%;background:var(--a)"></div></div><span class="bv">71/100</span></div>
        <div class="br"><span class="bl">B2B扩张</span><div class="bt"><div class="bf" style="width:60%;background:var(--a2)"></div></div><span class="bv">60/100</span></div>
        <div class="br"><span class="bl">数字化转型</span><div class="bt"><div class="bf" style="width:45%;background:var(--pu)"></div></div><span class="bv">45/100</span></div>
        <div class="br"><span class="bl">大湾区布局</span><div class="bt"><div class="bf" style="width:30%;background:var(--a4)"></div></div><span class="bv">30/100</span></div>
      </div>
    </div>
  </div>
  <div class="g32">'''
content = content.replace(old_g32, new_g32, 1)
print('gauge: OK' if 'gauge-health' in content else 'gauge: FAIL')

# 4. Add word cloud to P3 market page - after the g2 div
wc_card = '''
  <div class="card" style="margin-bottom:12px">
    <div class="ch"><span class="ct">舆情热词云（近7日）</span><span class="ca">实时更新</span></div>
    <div class="word-cloud">
      <span class="wc-word" style="font-size:28px;color:#f43f5e">5G套餐</span>
      <span class="wc-word" style="font-size:22px;color:#3b82f6">降价</span>
      <span class="wc-word" style="font-size:20px;color:#f59e0b">频谱</span>
      <span class="wc-word" style="font-size:18px;color:#22c55e">大湾区</span>
      <span class="wc-word" style="font-size:26px;color:#fb923c">价格战</span>
      <span class="wc-word" style="font-size:16px;color:#818cf8">边缘计算</span>
      <span class="wc-word" style="font-size:14px;color:#7e96b4">eSIM</span>
      <span class="wc-word" style="font-size:24px;color:#3b82f6">流失率</span>
      <span class="wc-word" style="font-size:16px;color:#22d3ee">Starlink</span>
      <span class="wc-word" style="font-size:19px;color:#f43f5e">客服投诉</span>
      <span class="wc-word" style="font-size:15px;color:#22c55e">AI网络</span>
      <span class="wc-word" style="font-size:21px;color:#f59e0b">OFCA</span>
      <span class="wc-word" style="font-size:13px;color:#7e96b4">工单</span>
      <span class="wc-word" style="font-size:17px;color:#818cf8">5G-A</span>
      <span class="wc-word" style="font-size:15px;color:#22d3ee">NPS提升</span>
      <span class="wc-word" style="font-size:23px;color:#3b82f6">企业专线</span>
      <span class="wc-word" style="font-size:14px;color:#f43f5e">合规</span>
      <span class="wc-word" style="font-size:18px;color:#22c55e">用户增长</span>
    </div>
  </div>
'''
# Insert before the competitor table in P3
old_p3_tbl = '  <div class="card" style="margin-bottom:12px"><div class="ch"><span class="ct">竞对关键指标'
new_p3_tbl = wc_card + '  <div class="card" style="margin-bottom:12px"><div class="ch"><span class="ct">竞对关键指标'
content = content.replace(old_p3_tbl, new_p3_tbl)
print('wordcloud: OK' if 'word-cloud' in content else 'wordcloud: FAIL')

open('/Users/liaowang/Desktop/需求56/index.html', 'w', encoding='utf-8').write(content)
print('Saved, lines:', content.count('\n'))
