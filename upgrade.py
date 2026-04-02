content = open('/Users/liaowang/Desktop/需求56/index.html', encoding='utf-8').read()

# 1. Add id to html tag
content = content.replace('<html lang="zh-CN">', '<html lang="zh-CN" id="root">')

# 2. Replace sfooter
old_sf = '  <div class="sfooter">\n    <button class="sync-btn" id="sync-btn" onclick="syncData()">同步数据</button>\n    <div class="sf-time" id="sf-time">--:--:--</div>\n  </div>'
new_sf = '  <div class="sfooter">\n    <div class="sfooter-btns">\n      <button class="sync-btn" id="sync-btn" onclick="syncData()">同步数据</button>\n      <button class="theme-btn" id="theme-btn" onclick="toggleTheme()" title="切换亮/暗色">☀</button>\n    </div>\n    <div class="sf-time" id="sf-time">--:--:--</div>\n  </div>'
if old_sf in content:
    content = content.replace(old_sf, new_sf)
    print('sfooter: OK')
else:
    print('sfooter: NOT FOUND')

# 3. Add search box above nav
old_nav = '  <nav class="nav">'
new_nav = '  <div class="search-wrap"><input class="search-box" id="search-box" placeholder="搜索模块..." oninput="searchNav(this.value)"></div>\n  <nav class="nav" id="main-nav">'
if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print('search: OK')
else:
    print('search: NOT FOUND')

# 4. Add notification panel to topbar - replace tb-r div
old_tbr = '    <div class="tb-r">\n      <span class="tb-time" id="tb-time">--:--:--</span>\n      <span class="bdg bdg-live">LIVE</span>\n    </div>'
new_tbr = '''    <div class="tb-r">
      <div class="notif-wrap" id="notif-wrap">
        <button class="notif-btn" onclick="toggleNotif()">通知<span class="notif-dot" id="notif-dot">4</span></button>
        <div class="notif-panel" id="notif-panel" style="display:none">
          <div class="notif-header"><span>系统通知</span><span class="ca" onclick="clearNotifs()">全部已读</span></div>
          <div class="notif-item ni-d-item"><div class="ni-icon"></div><div><div class="ni-msg">客户流失率逼近阈值 2.0%，需立即关注</div><div class="ni-time">2分钟前 · 高优先级</div></div></div>
          <div class="notif-item ni-w-item"><div class="ni-icon"></div><div><div class="ni-msg">3HK 新套餐 $138，低于市场均价 18%</div><div class="ni-time">18分钟前 · 竞对预警</div></div></div>
          <div class="notif-item ni-i-item"><div class="ni-icon"></div><div><div class="ni-msg">OFCA 频谱咨询截止 4月30日，请准备回应</div><div class="ni-time">1小时前 · 监管</div></div></div>
          <div class="notif-item ni-s-item"><div class="ni-icon"></div><div><div class="ni-msg">Q1 EBITDA 超出目标 2.3%，表现良好</div><div class="ni-time">3小时前 · 财务</div></div></div>
        </div>
      </div>
      <span class="tb-time" id="tb-time">--:--:--</span>
      <span class="bdg bdg-live">LIVE</span>
    </div>'''
if old_tbr in content:
    content = content.replace(old_tbr, new_tbr)
    print('notif: OK')
else:
    print('notif: NOT FOUND, trying partial match')
    idx = content.find('<div class="tb-r">')
    print('tb-r at:', idx)
    print('context:', repr(content[idx:idx+200]))

# 5. Add AI insight card before end of P0
ai_card = '''
<div class="card ai-card" style="margin-bottom:12px">
  <div class="ch"><span class="ct">AI 经营洞察摘要</span><span class="ca" onclick="refreshAI()">刷新分析</span></div>
  <div class="ai-body" id="ai-body">
    <div class="ai-item ai-good"><span class="ai-label">优势</span><span>5G渗透率71.3%领先市场3.4pts，企业专线增速+8.6%为各业务线最高，NPS连续两季改善。</span></div>
    <div class="ai-item ai-warn"><span class="ai-label">风险</span><span>流失率上升趋势需在本季度内遏制；3HK$138套餐直接冲击CMHK中低端用户群，建议48小时内完成定价应对方案。</span></div>
    <div class="ai-item ai-info"><span class="ai-label">机遇</span><span>大湾区互通协议开启跨境专线新市场；AI边缘计算需求爆发，建议优先布局深港双节点MEC。</span></div>
    <div class="ai-item ai-action"><span class="ai-label">行动</span><span>本周优先事项：①启动$158阻击套餐审批流程 ②提交OFCA频谱咨询回应草案 ③召开企业客户续签专项会议。</span></div>
  </div>
</div>
'''
# Insert before </div><!-- end content -->
if '</div><!-- end content -->' in content:
    content = content.replace('</div><!-- end content -->', ai_card + '</div><!-- end content -->')
    print('ai-card: OK')
else:
    print('ai-card anchor: NOT FOUND')

open('/Users/liaowang/Desktop/需求56/index.html', 'w', encoding='utf-8').write(content)
print('Saved, lines:', content.count('\n'))
