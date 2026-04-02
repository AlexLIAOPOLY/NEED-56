import re

content = open('/Users/liaowang/Desktop/需求56/index.html', encoding='utf-8').read()

# Replace the entire P5 scenario page HTML
old_p5_start = content.find('<!-- P5 场景模拟 -->')
old_p5_end = content.find('<!-- P6 行业趋势 -->')
old_p5 = content[old_p5_start:old_p5_end]

new_p5 = '''<!-- P5 场景模拟 -->
<div class="page" id="p5">
  <div class="g2">
    <div class="card">
      <div class="ch"><span class="ct">参数设置</span><span class="ca" onclick="resetScenario()">重置默认</span></div>
      <div class="sc"><div class="sc-lbl"><span>5G套餐均价（HKD）</span><span id="v-price">198</span></div><input type="range" min="120" max="280" value="198" id="s-price" oninput="updateScenario()"></div>
      <div class="sc"><div class="sc-lbl"><span>市场推广投入（百万HKD）</span><span id="v-mkt">85</span></div><input type="range" min="20" max="200" value="85" id="s-mkt" oninput="updateScenario()"></div>
      <div class="sc"><div class="sc-lbl"><span>网络建设投入（亿HKD）</span><span id="v-capex">28</span></div><input type="range" min="10" max="50" value="28" id="s-capex" oninput="updateScenario()"></div>
      <div class="sc"><div class="sc-lbl"><span>企业客户拓展目标（家）</span><span id="v-b2b">1200</span></div><input type="range" min="500" max="3000" value="1200" id="s-b2b" oninput="updateScenario()"></div>
      <div class="sc"><div class="sc-lbl"><span>5G覆盖目标（%）</span><span id="v-5g">75</span></div><input type="range" min="60" max="95" value="75" id="s-5g" oninput="updateScenario()"></div>
      <div class="sc"><div class="sc-lbl"><span>客户流失干预力度（%）</span><span id="v-churn">50</span></div><input type="range" min="0" max="100" value="50" id="s-churn" oninput="updateScenario()"></div>
      <div style="margin:14px 0 8px;font-size:10px;color:var(--t3);letter-spacing:1px;text-transform:uppercase">预测算法</div>
      <div class="algo-tabs" id="algo-tabs">
        <button class="algo-btn act" onclick="setAlgo(this,\'mc\')">蒙特卡洛</button>
        <button class="algo-btn" onclick="setAlgo(this,\'lr\')">线性回归</button>
        <button class="algo-btn" onclick="setAlgo(this,\'es\')">指数平滑</button>
        <button class="algo-btn" onclick="setAlgo(this,\'arima\')">ARIMA</button>
        <button class="algo-btn" onclick="setAlgo(this,\'bayes\')">贝叶斯</button>
      </div>
      <div class="algo-desc" id="algo-desc">蒙特卡洛：随机抽样10,000次模拟，给出概率分布置信区间</div>
      <div class="mc-status" id="mc-status">状态：就绪</div>
      <div class="mc-bar"><div class="mc-fill" id="mc-fill" style="width:0%"></div></div>
      <div class="sc-res">
        <div class="sc-res-title">12个月预测结果</div>
        <div class="sc-kpis">
          <div class="sc-kpi"><div class="sc-kv pos" id="sc-rev">+4.8%</div><div class="sc-kl">营收增长</div></div>
          <div class="sc-kpi"><div class="sc-kv pos" id="sc-usr">+8.2万</div><div class="sc-kl">净增用户</div></div>
          <div class="sc-kpi"><div class="sc-kv" id="sc-arpu">204</div><div class="sc-kl">预测ARPU</div></div>
          <div class="sc-kpi"><div class="sc-kv pos" id="sc-profit">+2.1pts</div><div class="sc-kl">利润率变化</div></div>
          <div class="sc-kpi"><div class="sc-kv" id="sc-churn">1.62%</div><div class="sc-kl">预测流失率</div></div>
          <div class="sc-kpi"><div class="sc-kv pos" id="sc-nps">+6pts</div><div class="sc-kl">NPS预测</div></div>
        </div>
        <div class="ci-row" id="ci-row"><span class="ci-label">82%置信区间</span><span class="ci-val" id="ci-val">+3.1% ~ +7.4%</span></div>
      </div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">场景雷达：基线 vs 模拟</span></div>
      <div class="cw h220"><canvas id="c-scenario"></canvas></div>
      <div style="margin-top:12px"><div class="ch"><span class="ct">算法对比：12月营收预测（亿HKD）</span><span class="ca" id="algo-rmse">RMSE: —</span></div>
        <div class="cw h180"><canvas id="c-algo-compare"></canvas></div>
      </div>
    </div>
  </div>
  <div class="g3">
    <div class="card">
      <div class="ch"><span class="ct">收入预测走势（含置信带）</span></div>
      <div class="cw h200"><canvas id="c-forecast"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">ROI敏感性分析</span></div>
      <div class="cw h200"><canvas id="c-roi"></canvas></div>
    </div>
    <div class="card">
      <div class="ch"><span class="ct">决策建议</span></div>
      <div class="alt alt-s">维持5G建设节奏，优先提升新界离岛覆盖至85%</div>
      <div class="alt alt-i">差异化定价：$158入门阻击3HK，$248强化高端感知</div>
      <div class="alt alt-w">B2B强化：增派20名客户经理，聚焦金融和物流</div>
      <div class="alt alt-s">数字服务加速API开放，打造第二增长曲线</div>
    </div>
  </div>
</div>

'''

content = content[:old_p5_start] + new_p5 + content[old_p5_end:]
open('/Users/liaowang/Desktop/需求56/index.html', 'w', encoding='utf-8').write(content)
print('P5 updated, lines:', content.count('\n'))
