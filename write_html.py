import textwrap

html = """<!DOCTYPE html>
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
</aside>"""

print("Part 1 written:", len(html))
open('/Users/liaowang/Desktop/需求56/index.html', 'w', encoding='utf-8').write(html)
