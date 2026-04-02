css = """
  font-weight:500;letter-spacing:.5px;text-transform:uppercase;
}
.tbl td{padding:8px 10px;border-bottom:1px solid rgba(26,36,54,.8);color:var(--t2);}
.tbl tr:last-child td{border-bottom:none;}
.tbl tr:hover td{background:rgba(59,130,246,.03);}
.tbl td.hi{color:var(--t);font-weight:500;}
.tag{display:inline-block;padding:1px 7px;border-radius:3px;font-size:10px;font-weight:500;}
.tg{background:rgba(34,197,94,.1);color:#22c55e;}
.tr2{background:rgba(244,63,94,.1);color:#f43f5e;}
.ta{background:rgba(245,158,11,.1);color:#f59e0b;}
.tb2{background:rgba(59,130,246,.1);color:#60a5fa;}
.tc{background:rgba(6,182,212,.1);color:#22d3ee;}
.tp{background:rgba(129,140,248,.1);color:#818cf8;}
.br{display:flex;align-items:center;gap:8px;margin-bottom:9px;}
.bl{font-size:11px;color:var(--t2);min-width:68px;}
.bt{flex:1;height:4px;background:rgba(255,255,255,.04);border-radius:2px;overflow:hidden;}
.bf{height:100%;border-radius:2px;transition:width 1.2s ease;}
.bv{font-size:11px;color:var(--t2);min-width:34px;text-align:right;}
.fi{padding:8px 0;border-bottom:1px solid rgba(26,36,54,.6);display:flex;gap:9px;}
.fi:last-child{border-bottom:none;}
.fd{width:5px;height:5px;border-radius:50%;margin-top:5px;flex-shrink:0;}
.ft{font-size:12px;color:var(--t);line-height:1.5;}
.fm{font-size:10px;color:var(--t3);margin-top:2px;}
.alt{display:flex;align-items:flex-start;gap:8px;padding:8px 11px;border-radius:5px;margin-bottom:7px;font-size:12px;line-height:1.5;}
.alt:last-child{margin-bottom:0;}
.alt-w{background:rgba(251,146,60,.07);border:1px solid rgba(251,146,60,.15);color:var(--wn);}
.alt-d{background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.15);color:var(--dn);}
.alt-i{background:rgba(59,130,246,.07);border:1px solid rgba(59,130,246,.15);color:var(--a2);}
.alt-s{background:rgba(34,197,94,.07);border:1px solid rgba(34,197,94,.15);color:var(--a3);}
.rm-grid{display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(5,32px);gap:3px;}
.rc{border-radius:3px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:transform .1s,filter .1s;position:relative;}
.rc:hover{transform:scale(1.1);filter:brightness(1.3);z-index:2;}
.rc-tip{position:absolute;bottom:calc(100%+6px);left:50%;transform:translateX(-50%);background:var(--bg4);border:1px solid var(--border2);color:var(--t);font-size:10px;padding:4px 10px;border-radius:4px;white-space:nowrap;display:none;z-index:30;pointer-events:none;}
.rc:hover .rc-tip{display:block;}
.rm-xl{font-size:9px;color:var(--t3);text-align:center;}
.rm-xlabels{display:grid;grid-template-columns:repeat(5,1fr);gap:3px;margin-top:5px;}
.sc{margin-bottom:13px;}
.sc-lbl{display:flex;justify-content:space-between;font-size:11.5px;color:var(--t2);margin-bottom:5px;}
.sc-lbl span:last-child{color:var(--a2);font-weight:600;}
input[type=range]{-webkit-appearance:none;width:100%;height:3px;border-radius:2px;background:var(--border2);outline:none;cursor:pointer;}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:var(--a);box-shadow:0 0 0 2px rgba(59,130,246,.3);}
.sc-res{background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:12px;margin-top:12px;}
.sc-res-title{font-size:9.5px;color:var(--t3);margin-bottom:10px;letter-spacing:.8px;text-transform:uppercase;}
.sc-kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
.sc-kpi{text-align:center;}
.sc-kv{font-size:18px;font-weight:700;color:var(--a2);transition:all .3s;}
.sc-kl{font-size:9px;color:var(--t3);margin-top:2px;}
.sc-kv.pos{color:var(--a3);}.sc-kv.neg{color:var(--dn);}
.mc-bar{height:3px;background:var(--border2);border-radius:2px;overflow:hidden;margin:8px 0;}
.mc-fill{height:100%;background:var(--a);border-radius:2px;transition:width .05s linear;}
.mc-status{font-size:10px;color:var(--t3);margin-bottom:4px;}
.msr{display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid rgba(26,36,54,.5);font-size:12px;}
.msr:last-child{border-bottom:none;}
.msr-l{color:var(--t2);}.msr-r{color:var(--t);font-weight:500;}
.alert-stream{max-height:220px;overflow-y:auto;}
.alert-stream::-webkit-scrollbar{width:3px;}
.alert-stream::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px;}
.stream-item{display:flex;align-items:flex-start;gap:8px;padding:7px 0;border-bottom:1px solid rgba(26,36,54,.4);animation:slide-in .3s ease;}
.stream-item:last-child{border-bottom:none;}
@keyframes slide-in{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}
.stream-dot{width:5px;height:5px;border-radius:50%;flex-shrink:0;margin-top:5px;}
.stream-text{font-size:11.5px;color:var(--t);line-height:1.4;}
.stream-time{font-size:9.5px;color:var(--t3);margin-top:2px;}
.divider{height:1px;background:var(--border);margin:12px 0;}
.sy{overflow-y:auto;}
.sy::-webkit-scrollbar{width:3px;}
.sy::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px;}
.slb{font-size:9px;color:var(--t3);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:8px;margin-top:2px;}
.filter-bar{display:flex;align-items:center;gap:8px;padding:8px 20px;background:var(--bg2);border-bottom:1px solid var(--border);}
.fb-label{font-size:10.5px;color:var(--t3);margin-right:4px;}
.fb-btn{padding:4px 12px;border-radius:4px;font-size:11px;cursor:pointer;background:transparent;border:1px solid var(--border);color:var(--t2);transition:all .12s;}
.fb-btn:hover{border-color:var(--a);color:var(--a2);}
.fb-btn.act{background:rgba(59,130,246,.12);border-color:var(--a);color:var(--a2);}
.fb-export{margin-left:auto;padding:4px 12px;border-radius:4px;font-size:11px;cursor:pointer;background:transparent;border:1px solid var(--border2);color:var(--t2);transition:all .12s;}
.fb-export:hover{border-color:var(--a3);color:var(--a3);}
"""
with open('/Users/liaowang/Desktop/需求56/style.css', 'a') as f:
    f.write(css)
print('done')
