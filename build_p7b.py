p7_part2 = '''
  <div class="g3">
    <div class="card cs2">
      <div class="ch"><span class="ct">实时数据流</span><span class="ca" id="stream-rate">加载中...</span></div>
      <div class="data-stream" id="data-stream"></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">数据接入量趋势</span></div>
      <div class="cw h200"><canvas id="c-ingest"></canvas></div>
    </div>
  </div>
  <div class="g3">
    <div class="card">
      <div class="ch"><span class="ct">数据质量监控</span></div>
      <div class="br"><span class="bl">完整性</span><div class="bt"><div class="bf" style="width:98%;background:var(--a3)"></div></div><span class="bv">98%</span></div>
      <div class="br"><span class="bl">准确性</span><div class="bt"><div class="bf" style="width:97%;background:var(--a3)"></div></div><span class="bv">97%</span></div>
      <div class="br"><span class="bl">及时性</span><div class="bt"><div class="bf" style="width:95%;background:var(--a)"></div></div><span class="bv">95%</span></div>
      <div class="br"><span class="bl">一致性</span><div class="bt"><div class="bf" style="width:94%;background:var(--a)"></div></div><span class="bv">94%</span></div>
      <div class="br"><span class="bl">唯一性</span><div class="bt"><div class="bf" style="width:99%;background:var(--a3)"></div></div><span class="bv">99%</span></div>
      <div class="divider"></div>
      <div class="msr"><span class="msr-l">异常记录（今日）</span><span class="msr-r" style="color:var(--wn)">3,421 条</span></div>
      <div class="msr"><span class="msr-l">自动修复率</span><span class="msr-r" style="color:var(--a3)">91.2%</span></div>
      <div class="msr"><span class="msr-l">人工介入</span><span class="msr-r">302 条</span></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">数据处理管道</span></div>
      <div class="pipeline">
        <div class="pl-step pl-done"><div class="pl-dot"></div><div><div class="pl-name">采集层</div><div class="pl-desc">Kafka · 24源 · 12.4万条/s</div></div></div>
        <div class="pl-arrow"></div>
        <div class="pl-step pl-done"><div class="pl-dot"></div><div><div class="pl-name">清洗层</div><div class="pl-desc">Flink · 去重/补全/格式化</div></div></div>
        <div class="pl-arrow"></div>
        <div class="pl-step pl-done"><div class="pl-dot"></div><div><div class="pl-name">融合层</div><div class="pl-desc">Spark · 内外部数据关联</div></div></div>
        <div class="pl-arrow"></div>
        <div class="pl-step pl-active"><div class="pl-dot pl-pulse"></div><div><div class="pl-name">分析层</div><div class="pl-desc">ClickHouse · OLAP · 实时计算中</div></div></div>
        <div class="pl-arrow"></div>
        <div class="pl-step pl-done"><div class="pl-dot"></div><div><div class="pl-name">服务层</div><div class="pl-desc">API Gateway · 决策仿真系统</div></div></div>
      </div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">最新采集事件</span></div>
      <div class="ds-list" id="event-feed"></div>
    </div>
  </div>
</div>
'''
open('/Users/liaowang/Desktop/需求56/p7_part2.txt', 'w', encoding='utf-8').write(p7_part2)
print('part2 written:', len(p7_part2))
