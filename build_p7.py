p7_part1 = '''
<!-- P7 数据接入 -->
<div class="page" id="p7">
  <div class="g4">
    <div class="kpi"><div class="kl">接入数据源</div><div class="kv">24<span class="ku">个</span></div><div class="kc up">↑ 3 本月新增</div></div>
    <div class="kpi"><div class="kl">今日数据包</div><div class="kv"><span id="pkt-count">1,284</span><span class="ku">万条</span></div><div class="kc up">实时增长中</div></div>
    <div class="kpi"><div class="kl">数据新鲜度</div><div class="kv">98.4<span class="ku">%</span></div><div class="kc up">延迟 <span id="latency">1.2</span>s 内</div></div>
    <div class="kpi"><div class="kl">数据质量评分</div><div class="kv">96.7<span class="ku">分</span></div><div class="kc up">↑ 1.2 较上月</div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="ch"><span class="ct">内部数据源</span><span class="ca" style="color:var(--a3)">7/8 在线</span></div>
      <div class="ds-list">
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">BSS 计费系统</div><div class="ds-meta">Oracle · 每5min · 用户账单/套餐数据</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-bss"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">OSS 网管平台</div><div class="ds-meta">Huawei iMaster · 实时 · 网络KPI/告警</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-oss"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">CRM 客户系统</div><div class="ds-meta">Salesforce · 每15min · 客户行为/NPS</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-crm"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">ERP 财务系统</div><div class="ds-meta">SAP S/4HANA · 每小时 · 收入/成本/利润</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-erp"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">工单系统</div><div class="ds-meta">ServiceNow · 实时 · 故障/投诉/工单</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-warn"></div><div class="ds-info"><div class="ds-name">渠道POS系统</div><div class="ds-meta">自研 · 每30min · 门店销售/库存</div></div><div class="ds-stat"><span class="tag ta">延迟</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">DPI 流量分析</div><div class="ds-meta">Deep Packet · 实时 · 用户行为/流量</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-dpi"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">HR 人力系统</div><div class="ds-meta">Workday · 每日 · 人员/绩效/离职率</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
      </div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">外部数据源</span><span class="ca" style="color:var(--wn)">1个异常</span></div>
      <div class="ds-list">
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">OFCA 监管数据</div><div class="ds-meta">官方API · 每日 · 频谱政策/合规指标</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">竞对情报爬虫</div><div class="ds-meta">自研Spider · 每6h · CSL/3HK/SmarTone套餐</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-spider"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">香港统计处</div><div class="ds-meta">census.gov.hk · 每月 · GDP/人口/消费</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-err"></div><div class="ds-info"><div class="ds-name">Global Telecom DB</div><div class="ds-meta">Ovum API · 每周 · 全球运营商KPI基准</div></div><div class="ds-stat"><span class="tag tr2">断连</span><span class="ds-retry" onclick="retrySource(this)">重连</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">新闻舆情监控</div><div class="ds-meta">NLP引擎 · 实时 · 媒体/社交/新闻</div></div><div class="ds-stat"><span class="tag tg">正常</span><div class="ds-spark" id="r-news"></div></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">金融市场数据</div><div class="ds-meta">Bloomberg API · 实时 · 汇率/利率/大盘</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">大湾区政务数据</div><div class="ds-meta">政务云API · 每日 · 跨境政策/企业注册</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
        <div class="ds-item"><div class="ds-dot ds-live"></div><div class="ds-info"><div class="ds-name">行业分析报告</div><div class="ds-meta">Gartner/IDC · 每季 · 行业报告/预测</div></div><div class="ds-stat"><span class="tag tg">正常</span></div></div>
      </div>
    </div>
  </div>
'''
open('/Users/liaowang/Desktop/需求56/p7_part1.txt', 'w', encoding='utf-8').write(p7_part1)
print('part1 written:', len(p7_part1))
