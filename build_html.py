# Build complete index.html
import os

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CMHK 决策仿真系统</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body>
<aside class="sidebar">
  <div class="slogo">
    <div class="sl-row"><div class="sl-mark">CK</div><div><div class="sl-name">CMHK</div><div class="sl-sub">DECISION SIMULATION v2.0</div></div></div>
    <div class="sys-live"><div class="ldot"></div><span>实时数据同步中</span></div>
  </div>
  <nav class="nav">
    <div class="ngl">核心模块</div>
    <div class="ni act" onclick="goPage(this,0)"><span class="ni-d"></span>决策总览</div>
    <div class="ni" onclick="goPage(this,1)"><span class="ni-d"></span>财务分析</div>
    <div class="ni" onclick="goPage(this,2)"><span class="ni-d"></span>运营监控</div>
    <div class="ni" onclick="goPage(this,3)"><span class="ni-d"></span>市场洞察<span class="ni-b" id="mkt-badge">3</span></div>
    <div class="ngl" style="margin-top:4px">智能决策</div>
    <div class="ni" onclick="goPage(this,4)"><span class="ni-d"></span>风险研判<span class="ni-b" id="risk-badge">2</span></div>
    <div class="ni" onclick="goPage(this,5)"><span class="ni-d"></span>场景模拟</div>
    <div class="ni" onclick="goPage(this,6)"><span class="ni-d"></span>行业趋势</div>
  </nav>
  <div class="sfooter">
    <button class="sync-btn" id="sync-btn" onclick="syncData()">同步数据</button>
    <div class="sf-time" id="sf-time">--:--:--</div>
  </div>
</aside>
<div class="main">
  <div class="topbar">
    <span class="tb-title" id="tb-title">决策总览</span>
    <span class="tb-sep">/</span>
    <span class="tb-sub" id="tb-sub">实时经营数据 · 内外部环境整合分析</span>
    <div class="tb-r">
      <span class="tb-time" id="tb-time">--:--:--</span>
      <span class="bdg bdg-live">LIVE</span>
    </div>
  </div>
  <div class="filter-bar">
    <span class="fb-label">时间范围</span>
    <button class="fb-btn" onclick="setRange(this,\'1M\')">近1月</button>
    <button class="fb-btn act" onclick="setRange(this,\'3M\')">近3月</button>
    <button class="fb-btn" onclick="setRange(this,\'6M\')">近6月</button>
    <button class="fb-btn" onclick="setRange(this,\'1Y\')">近1年</button>
    <span class="fb-sep"></span>
    <button class="fb-btn" onclick="setRange(this,\'YTD\')">YTD</button>
    <button class="fb-export" onclick="exportCSV()">导出 CSV</button>
  </div>
  <div class="content">
'''

# P0
html += '''<!-- P0 决策总览 -->
<div class="page act" id="p0">
  <div class="g4">
    <div class="kpi k-up"><div class="kl">总用户数</div><div class="kv">312.4<span class="ku">万</span></div><div class="kc up">↑ 2.3% 同比</div><div class="ks">本月新增 6.8万</div></div>
    <div class="kpi k-up"><div class="kl">月度营收</div><div class="kv">18.6<span class="ku">亿HKD</span></div><div class="kc up">↑ 4.1% 同比</div><div class="ks">移动业务占比 68%</div></div>
    <div class="kpi k-warn"><div class="kl">综合 ARPU</div><div class="kv">198<span class="ku">HKD</span></div><div class="kc dn2">↓ 1.2% 同比</div><div class="ks">行业均值 187 HKD</div></div>
    <div class="kpi k-up"><div class="kl">净推荐值 NPS</div><div class="kv">62<span class="ku">分</span></div><div class="kc up">↑ 5pts 季度</div><div class="ks">行业 TOP 15%</div></div>
  </div>
  <div class="g4">
    <div class="kpi k-up"><div class="kl">5G 渗透率</div><div class="kv">71.3<span class="ku">%</span></div><div class="kc up">↑ 3.8pts 同比</div><div class="ks">目标 75%</div></div>
    <div class="kpi k-dn"><div class="kl">客户流失率</div><div class="kv">1.84<span class="ku">%</span></div><div class="kc dn2">↑ 0.2pts 预警</div><div class="ks">阈值 2.0%</div></div>
    <div class="kpi k-up"><div class="kl">网络可用率</div><div class="kv">99.96<span class="ku">%</span></div><div class="kc up">达标 SLA</div><div class="ks">目标 99.95%</div></div>
    <div class="kpi k-up"><div class="kl">经营利润率</div><div class="kv">22.3<span class="ku">%</span></div><div class="kc up">↑ 1.1pts 同比</div><div class="ks">目标 24%</div></div>
  </div>
  <div class="g32">
    <div class="card">
      <div class="ch"><span class="ct">月度营收趋势（亿 HKD）</span><span class="ca" onclick="exportCSV()">导出</span></div>
      <div class="cw h200"><canvas id="c-rev-chart"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">业务结构占比</span></div>
      <div class="cw h200"><canvas id="c-biz"></canvas></div>
    </div>
  </div>
  <div class="g3">
    <div class="card">
      <div class="ch"><span class="ct">实时告警流</span><span class="ca" id="alert-count" style="color:var(--dn)">4 条未读</span></div>
      <div class="alert-stream" id="alert-stream"></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">用户结构（万人）</span></div>
      <div class="cw h160"><canvas id="c-usr"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">关键运营指标</span></div>
      <div class="br"><span class="bl">5G 占比</span><div class="bt"><div class="bf" style="width:71%;background:var(--a)"></div></div><span class="bv">71%</span></div>
      <div class="br"><span class="bl">宽带渗透</span><div class="bt"><div class="bf" style="width:58%;background:var(--a2)"></div></div><span class="bv">58%</span></div>
      <div class="br"><span class="bl">企业占比</span><div class="bt"><div class="bf" style="width:34%;background:var(--a3)"></div></div><span class="bv">34%</span></div>
      <div class="br"><span class="bl">国际业务</span><div class="bt"><div class="bf" style="width:22%;background:var(--a4)"></div></div><span class="bv">22%</span></div>
      <div class="br"><span class="bl">数字服务</span><div class="bt"><div class="bf" style="width:15%;background:var(--pu)"></div></div><span class="bv">15%</span></div>
      <div class="br"><span class="bl">满意度</span><div class="bt"><div class="bf" style="width:82%;background:var(--a3)"></div></div><span class="bv">82%</span></div>
    </div>
  </div>
</div>
'''

# P1
html += '''<!-- P1 财务分析 -->
<div class="page" id="p1">
  <div class="g4">
    <div class="kpi k-up"><div class="kl">年度营收</div><div class="kv">221.8<span class="ku">亿HKD</span></div><div class="kc up">↑ 3.8%</div></div>
    <div class="kpi k-up"><div class="kl">EBITDA</div><div class="kv">74.2<span class="ku">亿</span></div><div class="kc up">↑ 5.2% · 利润率33.5%</div></div>
    <div class="kpi k-warn"><div class="kl">资本开支</div><div class="kv">28.4<span class="ku">亿</span></div><div class="kc dn2">↓ 6.1% 优化中</div></div>
    <div class="kpi k-up"><div class="kl">自由现金流</div><div class="kv">45.8<span class="ku">亿</span></div><div class="kc up">↑ 12.3%</div></div>
  </div>
  <div class="g21">
    <div class="card">
      <div class="ch"><span class="ct">季度收入拆解（亿HKD）</span><span class="ca" onclick="exportCSV()">导出 CSV</span></div>
      <div class="cw h240"><canvas id="c-fin1"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">成本结构分布</span></div>
      <div class="cw h240"><canvas id="c-cost"></canvas></div>
    </div>
  </div>
  <div class="g3">
    <div class="card cs2">
      <div class="ch"><span class="ct">净利润 &amp; EBITDA 趋势（百万HKD）</span></div>
      <div class="cw h200"><canvas id="c-profit"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">财务健康指标</span></div>
      <div class="msr"><span class="msr-l">资产负债率</span><span class="msr-r">42.3%</span></div>
      <div class="msr"><span class="msr-l">流动比率</span><span class="msr-r">1.38</span></div>
      <div class="msr"><span class="msr-l">净利润率</span><span class="msr-r">22.3%</span></div>
      <div class="msr"><span class="msr-l">ROE</span><span class="msr-r">18.7%</span></div>
      <div class="msr"><span class="msr-l">ROA</span><span class="msr-r">8.4%</span></div>
      <div class="msr"><span class="msr-l">Capex/Rev</span><span class="msr-r">12.8%</span></div>
    </div>
  </div>
  <div class="card" style="margin-bottom:12px">
    <div class="ch"><span class="ct">分业务线财务明细（2026Q1）</span><span class="ca" onclick="exportCSV()">导出</span></div>
    <table class="tbl"><thead><tr><th>业务线</th><th>营收（亿）</th><th>同比</th><th>毛利率</th><th>净利润（亿）</th><th>收入贡献</th><th>状态</th></tr></thead>
    <tbody>
      <tr><td class="hi">移动通信</td><td>150.6</td><td><span class="tag tg">+4.2%</span></td><td>48.3%</td><td>28.6</td><td>67.9%</td><td><span class="tag tb2">稳健</span></td></tr>
      <tr><td class="hi">固网宽带</td><td>32.4</td><td><span class="tag tg">+2.1%</span></td><td>41.7%</td><td>6.8</td><td>14.6%</td><td><span class="tag tg">增长</span></td></tr>
      <tr><td class="hi">企业专线</td><td>24.8</td><td><span class="tag tg">+8.6%</span></td><td>55.2%</td><td>7.2</td><td>11.2%</td><td><span class="tag tg">高增长</span></td></tr>
      <tr><td class="hi">国际漫游</td><td>8.6</td><td><span class="tag tr2">-3.4%</span></td><td>38.1%</td><td>1.2</td><td>3.9%</td><td><span class="tag ta">承压</span></td></tr>
      <tr><td class="hi">数字服务</td><td>5.4</td><td><span class="tag tg">+22.3%</span></td><td>62.8%</td><td>1.8</td><td>2.4%</td><td><span class="tag tp">成长期</span></td></tr>
    </tbody></table>
  </div>
</div>
'''

# P2
html += '''<!-- P2 运营监控 -->
<div class="page" id="p2">
  <div class="g4">
    <div class="kpi k-up"><div class="kl">网络可用率</div><div class="kv">99.96<span class="ku">%</span></div><div class="kc up">达标 SLA</div></div>
    <div class="kpi k-up"><div class="kl">5G 小区数</div><div class="kv">8,642<span class="ku">个</span></div><div class="kc up">↑ 6.3%</div></div>
    <div class="kpi k-up"><div class="kl">平均下载速率</div><div class="kv">387<span class="ku">Mbps</span></div><div class="kc up">↑ 18%</div></div>
    <div class="kpi k-warn"><div class="kl">月度投诉工单</div><div class="kv">1,248<span class="ku">件</span></div><div class="kc dn2">↑ 3.2% 关注</div></div>
  </div>
  <div class="g2">
    <div class="card"><div class="ch"><span class="ct">网络质量趋势</span></div><div class="cw h200"><canvas id="c-net"></canvas></div></div>
    <div class="card"><div class="ch"><span class="ct">用户净增趋势（万人）</span></div><div class="cw h200"><canvas id="c-grow"></canvas></div></div>
  </div>
  <div class="g3">
    <div class="card"><div class="ch"><span class="ct">地区5G覆盖率</span></div>
      <div class="br"><span class="bl">香港岛</span><div class="bt"><div class="bf" 