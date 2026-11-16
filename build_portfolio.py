import re

with open(r'd:\PortFolio\cursor-style-portfolio\index.html', 'r', encoding='utf-8') as f:
    orig_lines = f.readlines()

font1 = orig_lines[8] # Big Shoulders Display
font2 = orig_lines[9] # Bricolage Grotesque

html_template = '''<!DOCTYPE html>
<html lang="en" class="locked">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yash Sojitra — Full Stack Blockchain & Web3 Developer</title>
<meta name="description" content="Portfolio of Yash Sojitra. Full Stack Blockchain Developer specializing in Solidity, Hyperledger Fabric, Rust smart contracts, IPFS, DeFi, Next.js, and enterprise security.">
<link rel="icon" type="image/png" href="assets/avatar.png">
<style>
''' + font1 + font2 + '''
@property --acc{syntax:"<color>";inherits:true;initial-value:#77777c}

:root{
  --ink:#050506; --ink2:#0e0e11; --paper:#f4f2ec; --mute:#94928b; --line:rgba(244,242,236,.13);
  --acc:#77777c; --on-acc:#050506; --sel:#1f9dff;
  --pad:clamp(18px,3.4vw,56px);
  --display:"Big Shoulders Display","Arial Narrow",Impact,sans-serif;
  --body:"Bricolage Grotesque",system-ui,-apple-system,"Segoe UI",sans-serif;
}
*{box-sizing:border-box;margin:0}
html{background:var(--ink);transition:--acc .55s ease;scrollbar-width:thin;scrollbar-color:#2a2a2e var(--ink)}
html.locked{overflow:hidden}
html.clean, html.clean *, html.nocursor, html.nocursor *{cursor:none !important}
body{position:relative;min-height:100vh;color:var(--paper);font:400 clamp(15px,1.02vw,17px)/1.55 var(--body);-webkit-font-smoothing:antialiased;
  background:
    radial-gradient(ellipse 90% 60% at 50% -10%, color-mix(in srgb,var(--acc) 14%,transparent), transparent 70%),
    linear-gradient(180deg, var(--ink) 0%, #08080a 100%);
}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background-image:radial-gradient(rgba(255,255,255,.06) 1px, transparent 1px);background-size:28px 28px;mask-image:radial-gradient(ellipse 80% 60% at 50% 30%, #000 30%, transparent 80%);-webkit-mask-image:radial-gradient(ellipse 80% 60% at 50% 30%, #000 30%, transparent 80%)}

a{color:inherit;text-decoration:none}
button{font-family:inherit}
a:focus-visible,button:focus-visible{outline:2px solid var(--sel);outline-offset:3px}
::selection{background:var(--acc);color:var(--on-acc)}

/* ---------- build states ---------- */
[data-b]{opacity:0}
[data-b].on{opacity:1;transition:opacity .22s ease}
.ch{opacity:0;display:inline!important;padding:0!important;border:0!important;background:none!important;margin:0!important;font:inherit!important;color:inherit!important}.ch.v{opacity:1}

/* ---------- hero ---------- */
.hero{height:100svh;min-height:680px;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.82fr) minmax(0,.9fr);grid-template-rows:auto auto minmax(0,1fr) auto;column-gap:clamp(20px,3.2vw,56px);padding:0 var(--pad) clamp(76px,10vh,100px)}
.nav{grid-column:1/-1;display:flex;align-items:center;gap:clamp(14px,2.4vw,34px);padding:18px 0 14px;font-size:14px}
.brand{display:flex;align-items:center;gap:10px;font-weight:600;margin-right:auto}
.logo{display:grid;place-items:center;width:32px;height:32px;background:var(--acc);color:var(--on-acc);font:900 18px/1 var(--display);letter-spacing:.02em;border-radius:4px}
.nav nav{display:flex;gap:clamp(12px,2vw,28px);color:var(--mute)}
.nav nav a:hover{color:var(--paper)}
.avail{display:flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid var(--line);white-space:nowrap;border-radius:999px;font-size:13px}
.avail i{width:7px;height:7px;border-radius:50%;background:#3ddc84;box-shadow:0 0 0 0 #3ddc84;animation:ping 2s infinite}
@keyframes ping{70%{box-shadow:0 0 0 7px transparent}100%{box-shadow:0 0 0 0 transparent}}

.mega{grid-column:1/-1;display:block;width:100%;height:auto;max-height:28vh;overflow:visible;filter:drop-shadow(0 0 22px color-mix(in srgb,var(--acc) 38%,transparent))}
.mega text{font:900 300px/1 var(--display);fill:color-mix(in srgb,var(--acc) 7%,transparent);stroke:var(--acc);stroke-width:2.6;stroke-linejoin:round;stroke-dasharray:2400;stroke-dashoffset:2400;paint-order:stroke}

.intro{grid-column:1;position:relative;z-index:2;margin-top:clamp(-76px,-5.4vw,-22px);align-self:start}
.hello{display:inline-block;font-weight:600;font-size:clamp(19px,1.7vw,27px);transform:rotate(-4deg);transform-origin:left bottom;margin:0 0 4px 4px;text-shadow:0 2px 14px var(--ink)}
.name{display:block;width:max-content;background:var(--acc);color:var(--on-acc);font:900 clamp(54px,6.8vw,110px)/.8 var(--display);padding:.13em .16em .05em;letter-spacing:.01em}
.role{display:flex;align-items:center;gap:10px;margin-top:clamp(14px,2.2vh,24px);font-weight:600;font-size:clamp(14px,1.05vw,17px)}
.role i{width:8px;height:8px;background:var(--acc);flex:none}
.lede{max-width:34em;margin-top:clamp(10px,1.8vh,18px);font-size:clamp(15.5px,1.2vw,19px);line-height:1.45;color:#d9d6ce}
.lede b{color:var(--paper);font-weight:700}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:clamp(16px,2.6vh,28px)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:12px 18px;font-weight:700;font-size:14.5px;border:1px solid var(--line);background:rgba(244,242,236,.04);border-radius:4px;transition:border-color .2s, background .2s}
.btn.pri{background:var(--acc);color:var(--on-acc);border-color:transparent}
.btn:hover{border-color:var(--paper);background:rgba(244,242,236,.08)}
.btn.pri:hover{filter:brightness(1.08)}
.btn svg{width:16px;height:16px;fill:currentColor}

.portrait{grid-column:2;align-self:stretch;justify-self:stretch;container-type:size;display:grid;place-items:center;min-height:0;margin-top:clamp(10px,2.4vh,26px)}
.pwrap{position:relative;width:calc(min(100cqw,100cqh) - 22px);height:calc(min(100cqw,100cqh) - 22px)}
.disc{position:absolute;inset:0;border-radius:50%;overflow:hidden;background:var(--acc);outline:1px solid rgba(255,255,255,.25);outline-offset:5px;box-shadow:0 12px 40px rgba(0,0,0,.6)}
.disc img{display:block;width:100%;height:100%;object-fit:cover;object-position:center;transform:scale(1.12);transition:transform .4s}
.disc.on img{transform:none}
html:not(.inked) .disc img{filter:grayscale(1) contrast(1.08)}
.tagline{position:absolute;left:50%;bottom:-28px;transform:translateX(-50%);white-space:nowrap;font-size:12px;color:var(--mute);letter-spacing:.04em;text-transform:uppercase}

.now{grid-column:3;align-self:start;margin-top:clamp(-40px,-3.2vw,-8px);background:var(--ink2);border:1px solid var(--line);padding:clamp(14px,2.2vw,22px);border-radius:6px}
.now h2{font:700 11.5px/1 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--acc);margin-bottom:14px}
.now ul{list-style:none;display:flex;flex-direction:column;gap:12px;padding:0}
.now li{display:flex;flex-direction:column;gap:3px;font-size:13.5px;line-height:1.4}
.now strong{color:var(--paper);font-weight:700;font-size:14px}
.now span{color:var(--mute);font-size:13px}

.stats{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:clamp(16px,4vw,60px);align-items:flex-end;border-top:1px solid var(--line);padding-top:clamp(16px,2.5vh,26px);margin-top:clamp(10px,2vh,20px)}
.stat{display:flex;flex-direction:column}
.stat b{font:900 clamp(32px,3.6vw,52px)/.9 var(--display);letter-spacing:.02em;color:var(--acc)}
.stat span{color:var(--mute);font-size:13px;margin-top:5px}

/* ---------- sections ---------- */
.sec{padding:clamp(60px,10vh,110px) var(--pad);border-top:1px solid var(--line)}
.sec h2.h{font:900 clamp(44px,5.8vw,86px)/.9 var(--display);text-transform:uppercase;letter-spacing:.01em}
.sec p.sub{margin-top:12px;max-width:38em;color:var(--mute);font-size:clamp(16px,1.2vw,20px)}

.about{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(30px,6vw,80px);align-items:start}
.about p{color:#cfccc4;font-size:clamp(16px,1.15vw,18.5px);line-height:1.6;margin-top:16px}
.quote{margin-top:24px;padding:16px 20px;border-left:3px solid var(--acc);background:var(--ink2);color:var(--paper);font-size:16px;font-style:italic}
.time{list-style:none;padding:0;display:flex;flex-direction:column;gap:0;border-left:1px solid var(--line);margin-top:8px}
.time li{position:relative;padding:0 0 28px 24px;display:flex;flex-direction:column;gap:4px}
.time li:last-child{padding-bottom:0}
.time li::before{content:"";position:absolute;left:-5px;top:4px;width:9px;height:9px;border-radius:50%;background:var(--acc);outline:3px solid var(--ink)}
.time b{font:900 clamp(20px,1.8vw,26px)/1 var(--display);color:var(--acc)}
.time span{color:#cfccc4;font-size:14.5px;line-height:1.45}

/* ---------- Experience ---------- */
.exp-list{display:flex;flex-direction:column;gap:20px;margin-top:clamp(26px,5vh,44px)}
.exp-card{background:var(--ink2);border:1px solid var(--line);padding:clamp(20px,3vw,30px);display:flex;flex-direction:column;gap:12px;border-radius:6px;transition:border-color .2s}
.exp-card:hover{border-color:rgba(244,242,236,.3)}
.exp-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 16px;border-bottom:1px solid var(--line);padding-bottom:12px}
.exp-title-group{display:flex;flex-direction:column;gap:4px}
.exp-head h3{font:900 clamp(24px,2.4vw,34px)/1.05 var(--display);text-transform:uppercase;letter-spacing:.01em}
.exp-company{font-weight:700;font-size:15px;color:var(--acc)}
.exp-date{font-size:13.5px;color:var(--mute);font-weight:600}
.exp-points{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:8px;color:#cfccc4;font-size:15px;line-height:1.5}
.exp-points li::marker{color:var(--acc)}

/* ---------- cards (projects) ---------- */
.cards{margin-top:clamp(26px,5vh,48px);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{background:var(--ink2);border:1px solid var(--line);display:flex;flex-direction:column;border-radius:6px;overflow:hidden;transition:border-color .2s}
.card:hover{border-color:rgba(244,242,236,.35)}
.thumb{aspect-ratio:16/9;background:#09090b;border-bottom:1px solid var(--line);position:relative;overflow:hidden}
.thumb svg{position:absolute;inset:0;width:100%;height:100%}
.thumb .s{fill:none;stroke:var(--paper);stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}
.thumb .a{fill:var(--acc)}.thumb .as{fill:none;stroke:var(--acc);stroke-width:2;stroke-linecap:round}
.thumb .d{fill:rgba(244,242,236,.2)}
.card .body{padding:18px 18px 20px;display:flex;flex-direction:column;gap:8px;flex:1}
.kind{align-self:flex-start;font-size:11.5px;font-weight:700;padding:2px 8px;background:var(--acc);color:var(--on-acc);border-radius:3px;text-transform:uppercase;letter-spacing:.03em}
.kind.hw{background:transparent;color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}
.card h3{font:900 clamp(26px,2.4vw,36px)/.95 var(--display);text-transform:uppercase;letter-spacing:.01em}
.card p{color:#cfccc4;font-size:14.5px;line-height:1.45}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:10px}
.tags span{font-size:12px;color:var(--mute);border:1px solid var(--line);padding:2px 7px;border-radius:3px}

/* ---------- stack ---------- */
.stack{margin-top:clamp(26px,5vh,54px);display:grid;gap:0}
.row{display:grid;grid-template-columns:clamp(120px,16vw,240px) 1fr;gap:20px;align-items:center;padding:20px 0;border-top:1px solid var(--line)}
.row:last-child{border-bottom:1px solid var(--line)}
.row h3{font:700 15px/1.2 var(--body);color:var(--mute);text-transform:uppercase;letter-spacing:.04em}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chips span{font:800 clamp(20px,2.1vw,32px)/1 var(--display);text-transform:uppercase;letter-spacing:.02em;padding:8px 14px 6px;border:1px solid var(--line);background:var(--ink2);border-radius:4px}
.chips span.hot{background:var(--acc);color:var(--on-acc);border-color:transparent}

/* ---------- Credentials ---------- */
.cred-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px;margin-top:clamp(26px,5vh,44px)}
.cred-card{background:var(--ink2);border:1px solid var(--line);padding:22px;display:flex;flex-direction:column;gap:10px;border-radius:6px}
.cred-card .badge{align-self:flex-start;font-size:11.5px;font-weight:700;padding:2px 8px;background:var(--acc);color:var(--on-acc);border-radius:3px;text-transform:uppercase}
.cred-card .badge.award{background:transparent;color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}
.cred-card h3{font:900 clamp(22px,2vw,28px)/1.1 var(--display);text-transform:uppercase}
.cred-card p{color:#cfccc4;font-size:14px;line-height:1.45}
.cred-card .meta{margin-top:auto;font-size:13px;color:var(--mute);font-weight:600}

/* ---------- contact ---------- */
.contact{min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding-bottom:clamp(90px,14vh,130px)}
.swarm-stage{width:100%;height:clamp(150px,34vh,330px)}
.contact h2.h{max-width:none;margin-top:10px}
.contact .sub{margin-inline:auto}
.contact .cta{justify-content:center;margin-top:clamp(36px,5vh,54px)}
.foot{margin-top:clamp(48px,7vh,64px);color:var(--mute);font-size:13.5px;max-width:38em;margin-inline:auto}
kbd{font:600 12px/1 var(--body);padding:3px 6px;border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;color:var(--paper);background:rgba(255,255,255,.05)}

/* thumbnails motion */
@keyframes dash{to{stroke-dashoffset:-28}}
@keyframes hop{0%{transform:translateX(0);opacity:0}15%{opacity:1}85%{opacity:1}100%{transform:translateX(92px);opacity:0}}
@keyframes blink{0%,44%,52%,100%{transform:scaleY(1)}48%{transform:scaleY(.08)}}
@keyframes sweep{from{transform:rotate(-78deg)}to{transform:rotate(78deg)}}
@keyframes eq{0%,100%{transform:scaleY(.25)}50%{transform:scaleY(1)}}
@keyframes zone{0%,100%{opacity:.15}50%{opacity:1}}
.t-pk{animation:hop 1.6s linear infinite}
.t-eye{transform-box:fill-box;transform-origin:center;animation:blink 3.4s infinite}
.t-sweep{transform-origin:160px 150px;animation:sweep 2.2s ease-in-out infinite alternate}
.t-eq{transform-box:fill-box;transform-origin:bottom;animation:eq .9s ease-in-out infinite}
.t-zone{animation:zone 2s infinite}

/* ---------- the tool layer: agents, wires, HUD ---------- */
#stage{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:50}
.wire{position:absolute;border:1px solid var(--sel);background:rgba(150,160,178,.15);transition:opacity .16s, background .16s}
.wire.edit{background:rgba(31,157,255,.06)}
.wire.out{opacity:0}
.wire u{position:absolute;width:6px;height:6px;background:#fff;border:1px solid var(--sel)}
.wire u:nth-child(1){left:-3.5px;top:-3.5px}.wire u:nth-child(2){right:-3.5px;top:-3.5px}
.wire u:nth-child(3){left:-3.5px;bottom:-3.5px}.wire u:nth-child(4){right:-3.5px;bottom:-3.5px}
.wire em{position:absolute;left:50%;top:calc(100% + 5px);transform:translateX(-50%);background:var(--sel);color:#fff;font:600 10.5px/1 var(--body);padding:3px 5px 2px;border-radius:3px;white-space:nowrap;font-style:normal}
.wire.sm em{display:none}

.agent{position:absolute;left:0;top:0;width:0;height:0;will-change:transform;z-index:2}
.agent svg{position:absolute;overflow:visible;filter:drop-shadow(0 1px 3px rgba(0,0,0,.7))}
.agent .arrow{left:-2px;top:-1px;width:17px;height:22px}
.agent .cross,.agent .ibeam{left:-9px;top:-9px;width:18px;height:18px;display:none}
.agent[data-mode=cross] .arrow,.agent[data-mode=ibeam] .arrow{display:none}
.agent[data-mode=cross] .cross{display:block}.agent[data-mode=ibeam] .ibeam{display:block}
.agent label{position:absolute;left:13px;top:17px;font:700 11px/1 var(--body);padding:4px 7px 3px;border-radius:3px 9px 9px 9px;color:#050506;white-space:nowrap}
.agent[data-mode=cross] label,.agent[data-mode=ibeam] label{left:10px;top:10px}
.agent .ring{position:absolute;left:-14px;top:-14px;width:28px;height:28px;border-radius:50%;border:2px solid currentColor;opacity:0;transform:scale(.2)}
.agent.click .ring{animation:click .38s ease-out}
@keyframes click{0%{opacity:.9;transform:scale(.2)}100%{opacity:0;transform:scale(1.25)}}

.picker{position:absolute;display:flex;gap:9px;padding:10px;background:#1b1b20;border:1px solid rgba(255,255,255,.14);border-radius:12px;box-shadow:0 16px 40px rgba(0,0,0,.6);opacity:0;transform:translateY(6px) scale(.96);transition:.2s;z-index:1}
.picker.show{opacity:1;transform:none}
.picker i{width:26px;height:26px;border-radius:50%;box-shadow:inset 0 0 0 2px rgba(0,0,0,.25);cursor:pointer}
.picker i.sel{outline:2px solid #fff;outline-offset:2px}

#swarm{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:55}
.scan{position:fixed;left:0;right:0;top:0;height:2px;background:var(--sel);box-shadow:0 0 30px 6px rgba(31,157,255,.55);z-index:60;opacity:0;pointer-events:none}

.boot{position:fixed;inset:0;display:grid;place-items:center;z-index:40;pointer-events:none;transition:opacity .4s}
.boot.off{opacity:0}
.boot .chip{width:56px;height:56px;border-radius:14px;background:#1c1c21;border:1px solid rgba(255,255,255,.14);display:grid;place-items:center;font:900 26px/1 var(--display);color:var(--acc)}
.boot p{position:absolute;top:calc(50% + min(26vh,230px));left:0;right:0;text-align:center;color:var(--mute);font-size:15px;padding:0 20px}

/* ---------- HUD & Music pill ---------- */
.hud{position:fixed;left:50%;bottom:clamp(10px,2.4vh,22px);transform:translateX(-50%);z-index:70;display:flex;align-items:center;gap:12px;max-width:calc(100vw - 16px);padding:8px 8px 8px 12px;border-radius:999px;background:rgba(24,24,28,.88);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.12);box-shadow:0 12px 44px rgba(0,0,0,.6);font:600 12.5px/1 var(--body);color:#c9c8c3;white-space:nowrap;transition:opacity .25s, transform .25s}
html.clean .hud{opacity:0;transform:translate(-50%,20px);pointer-events:none}
.avs{display:flex}.avs i{width:15px;height:15px;border-radius:50%;margin-left:-5px;border:2px solid #18181c}.avs i:first-child{margin-left:0}
.hud .bar{width:clamp(40px,9vw,110px);height:3px;background:rgba(255,255,255,.12);border-radius:2px;overflow:hidden}
.hud .bar i{display:block;height:100%;width:0;background:var(--sel);transition:width .2s}
.hud .st{min-width:80px;color:#fff}
.hud button{all:unset;cursor:pointer;display:grid;place-items:center;height:28px;min-width:28px;padding:0 9px;border-radius:999px;background:rgba(255,255,255,.07);color:#fff;font:700 12.5px/1 var(--body)}
.hud button:hover{background:rgba(255,255,255,.16)}
.hud button.go{background:var(--sel)}
.hud button.tog{color:#8b8b90}.hud button.tog.on{color:#9fd4ff;box-shadow:inset 0 0 0 1px rgba(31,157,255,.7)}
.hud button svg{width:13px;height:13px;fill:currentColor}
.hud .mutedline{display:none}.hud .off .mutedline{display:block}

.music-pill{display:inline-flex!important;align-items:center;gap:7px;background:rgba(255,255,255,.07)!important;border-radius:999px!important;padding:0 11px!important;height:28px!important;cursor:pointer;border:1px solid rgba(255,255,255,.1);transition:border-color .2s}
.music-pill.playing{border-color:color-mix(in srgb,var(--acc) 60%,#fff)}
.music-pill.muted{opacity:.6}
.music-bars{display:inline-flex;align-items:flex-end;gap:2px;height:11px;width:11px}
.music-bars i{width:2px;height:100%;background:var(--acc);border-radius:1px;animation:mbar .75s ease-in-out infinite alternate}
.music-bars i:nth-child(2){animation-delay:.2s;height:60%}
.music-bars i:nth-child(3){animation-delay:.4s;height:80%}
.music-pill.muted .music-bars i{animation:none;height:25%;background:var(--mute)}
@keyframes mbar{0%{height:20%}100%{height:100%}}
.music-name{font-size:12px;color:var(--paper)}
.music-time{font-size:11.5px;color:var(--mute);font-family:monospace}

@media (max-width:860px){.hud .hide-s,.hud .avs{display:none}.hud{gap:8px;padding-left:14px}.hud .st{min-width:54px}.hud button{padding:0 7px}}
#stage label{transition:opacity .4s}#stage.ring label{opacity:0}

/* ---------- small screens ---------- */
@media (max-width:980px){
  .hero{height:auto;min-height:0;grid-template-columns:minmax(0,1fr) minmax(0,.8fr);grid-template-rows:auto auto auto auto auto}
  .intro{grid-column:1/-1}
  .portrait{grid-column:1;container-type:inline-size;align-self:start;margin-top:26px}
  .pwrap{width:calc(100cqw - 22px);height:calc(100cqw - 22px)}
  .now{grid-column:2;margin-top:26px;align-self:start}
  .cards{grid-template-columns:repeat(2,minmax(0,1fr))}
  .about{grid-template-columns:1fr}
}
@media (max-width:620px){
  .nav nav{display:none}
  .hero{grid-template-columns:1fr}
  .portrait,.now{grid-column:1}
  .portrait{width:74%;justify-self:start}
  .cards{grid-template-columns:1fr}
  .row{grid-template-columns:1fr;gap:12px}
  .stats{gap:18px 30px}
}
</style>
</head>
<body>

<audio id="bgMusic" src="assets/aura-farming.mp3" preload="auto"></audio>

<main id="page">

<!-- ================= HERO ================= -->
<section class="hero" id="top">
  <header class="nav" data-block>
    <a class="brand" href="#top" data-b="box"><span class="logo">YS</span><span>Yash Sojitra</span></a>
    <nav>
      <a href="#about" data-b="text">About</a>
      <a href="#experience" data-b="text">Experience</a>
      <a href="#work" data-b="text">Projects</a>
      <a href="#stack" data-b="text">Stack</a>
      <a href="#credentials" data-b="text">Credentials</a>
      <a href="#contact" data-b="text">Contact</a>
    </nav>
    <span class="avail" data-b="box"><i></i>Open to Web3 & Blockchain Roles</span>
  </header>

  <svg class="mega" data-block data-b="mega" preserveAspectRatio="none" aria-label="Blockchain Developer" role="img"><text>BLOCKCHAIN</text></svg>

  <div class="intro" data-block>
    <span class="hello" data-b="text">Hello, I'm</span>
    <h1 class="name" data-b="box">YASH.</h1>
    <p class="role" data-b="text"><i></i>Full Stack Blockchain & Web3 Developer</p>
    <p class="lede" data-b="text">Architecting decentralized dApps, zero-knowledge DeFi protocols, and enterprise smart contracts on <b>Solidity, Hyperledger Fabric, Rust, and Next.js</b>. Recognized by the <b>Ministry of Home Affairs</b> for cybersecurity excellence.</p>
    <div class="cta">
      <a class="btn pri" href="#work" data-b="box">See the work</a>
      <a class="btn" href="assets/Yash_Sojitra_Resume.pdf" target="_blank" rel="noopener" data-b="box">Download Resume</a>
      <a class="btn" data-link="github" href="https://github.com/sojitrayash" target="_blank" rel="noopener" data-b="box">GitHub</a>
      <a class="btn" data-link="linkedin" href="https://www.linkedin.com/in/sojitra-yashkumar" target="_blank" rel="noopener" data-b="box">LinkedIn</a>
    </div>
  </div>

  <figure class="portrait" data-block>
    <div class="pwrap">
      <div class="disc" data-b="box"><img alt="Yash Sojitra" id="photo" src="assets/avatar.png"></div>
      <figcaption class="tagline" data-b="text">Ahmedabad, Gujarat • Blockchain Engineer</figcaption>
    </div>
  </figure>

  <aside class="now" data-block>
    <h2 data-b="text">On the bench right now</h2>
    <ul>
      <li data-b="box"><strong data-b="text">BIMA Protocol (Arch Network)</strong><span data-b="text">Rust DeFi smart contracts on ZkVM with USBD stablecoin & Bitcoin Runes/Ordinals.</span></li>
      <li data-b="box"><strong data-b="text">Land Record Blockchain</strong><span data-b="text">Hyperledger Fabric enterprise network with Private Data Collections & Merkle batch anchoring.</span></li>
      <li data-b="box"><strong data-b="text">Academic Credentialing</strong><span data-b="text">One-click tamper-proof certificate generation on Polygon/Avalanche with zero-trust QR portal.</span></li>
    </ul>
  </aside>

  <div class="stats" data-block>
    <div class="stat" data-b="box"><b>9.10</b><span>Cumulative GPA (B.Tech IT)</span></div>
    <div class="stat" data-b="box"><b>3+</b><span>Industry Roles & Internships</span></div>
    <div class="stat" data-b="box"><b>6+</b><span>Production Web3 & AI Platforms</span></div>
    <div class="stat" data-b="box"><b>MHA</b><span>Cybersecurity Hack Proof Winner</span></div>
  </div>
</section>

<!-- ================= ABOUT ================= -->
<section class="sec about" id="about">
  <div data-block>
    <h2 class="h" data-b="text">How I got here</h2>
    <p data-b="text">I'm a B.Tech Information Technology student at Aditya Silver Oak Institute of Technology in Ahmedabad, Gujarat, graduating in July 2026 with a 9.10 / 10.0 CGPA.</p>
    <p data-b="text">I specialize in engineering high-security distributed systems: writing on-chain smart contracts in Solidity and Rust, architecting enterprise Hyperledger Fabric chaincode, integrating IPFS/Filecoin decentralized storage, and securing infrastructure through mTLS and PKI certificate authentication.</p>
    <p data-b="text">Whether developing stablecoin minting engines on Bitcoin L2s or deploying zero-knowledge verification pipelines for government and railway systems, I combine cryptographic rigor with modern Next.js/Node.js full-stack architectures.</p>
    <p class="quote" data-b="text">"Building secure, decentralised, and scalable solutions that bridge Web2 and Web3 with mathematical certainty."</p>
  </div>
  <ol class="time" data-block>
    <li data-b="box"><b data-b="text">2022</b><span data-b="text">Completed HSC Science (78%) from Dev International School; enrolled in B.Tech IT at Silver Oak University.</span></li>
    <li data-b="box"><b data-b="text">2023 - 2024</b><span data-b="text">Full Stack Developer Intern at PavitraSoft; developed REST APIs, Django backends, and responsive UIs.</span></li>
    <li data-b="box"><b data-b="text">2024</b><span data-b="text">Software Developer at Western Railway (S&T Institute); deployed production mTLS & X.509 certificate PKI authentication.</span></li>
    <li data-b="box"><b data-b="text">2025 - Present</b><span data-b="text">Full Stack Blockchain Developer at JadeQuest Consulting; building enterprise dApps, Hyperledger chaincode & DeFi mechanisms.</span></li>
  </ol>
</section>

<!-- ================= EXPERIENCE ================= -->
<section class="sec" id="experience">
  <div data-block>
    <h2 class="h" data-b="text">Work Experience</h2>
    <p class="sub" data-b="text">Hands-on enterprise roles in blockchain development, cybersecurity PKI, and full-stack engineering.</p>
  </div>
  <div class="exp-list">

    <article class="exp-card" data-block data-b="box">
      <div class="exp-head">
        <div class="exp-title-group">
          <h3 data-b="text">Full Stack Blockchain Developer</h3>
          <span class="exp-company" data-b="box">JadeQuest Consulting Pvt Ltd</span>
        </div>
        <span class="exp-date" data-b="text">Dec 2025 – Present</span>
      </div>
      <ul class="exp-points">
        <li data-b="text">Built end-to-end dApps bridging Web2 and Web3 using React/Next.js frontends and Node.js backends connected to on-chain smart contracts.</li>
        <li data-b="text">Authored Hyperledger Fabric chaincode (Go/Node.js) for asset management, audit trails, and multi-org endorsement workflows in permissioned enterprise networks.</li>
        <li data-b="text">Integrated IPFS and Filecoin for decentralised off-chain document storage, anchoring content hashes on-chain for tamper-proof verification.</li>
        <li data-b="text">Implemented role-based access control, multi-sig wallet patterns, and DeFi integrations including lending, borrowing, and stablecoin minting mechanisms.</li>
      </ul>
      <div class="tags" data-b="box">
        <span>Solidity</span><span>Hyperledger Fabric</span><span>Rust</span><span>IPFS</span><span>Filecoin</span><span>DeFi</span><span>Next.js</span><span>Node.js</span>
      </div>
    </article>

    <article class="exp-card" data-block data-b="box">
      <div class="exp-head">
        <div class="exp-title-group">
          <h3 data-b="text">Software Developer (Security & PKI)</h3>
          <span class="exp-company" data-b="box">S&T Training Institute – Western Railway (Sabarmati, Ahmedabad)</span>
        </div>
        <span class="exp-date" data-b="text">Apr 2024 – Jun 2024</span>
      </div>
      <ul class="exp-points">
        <li data-b="text">Designed and deployed a certificate-based authentication system for Western Railway, replacing password-based login with X.509 digital certificates issued via an internal Certificate Authority (CA).</li>
        <li data-b="text">Implemented SSL/TLS mutual authentication (mTLS) to enforce two-way identity verification between clients and servers, eliminating man-in-the-middle attack vectors.</li>
        <li data-b="text">Automated certificate issuance, renewal, and revocation lifecycle using OpenSSL and integrated CRL (Certificate Revocation List) checks into the authentication pipeline.</li>
        <li data-b="text">Built a secure admin portal for certificate management — enabling IT staff to issue, revoke, and audit employee certificates with full audit logging and RBAC.</li>
        <li data-b="text">Integrated the authentication system with existing enterprise SSO infrastructure, ensuring seamless login across internal applications without credential re-entry.</li>
      </ul>
      <div class="tags" data-b="box">
        <span>X.509</span><span>mTLS</span><span>OpenSSL</span><span>PKI</span><span>Enterprise SSO</span><span>Cybersecurity</span><span>Node.js</span>
      </div>
    </article>

    <article class="exp-card" data-block data-b="box">
      <div class="exp-head">
        <div class="exp-title-group">
          <h3 data-b="text">Full Stack Developer Intern</h3>
          <span class="exp-company" data-b="box">PavitraSoft (Remote, Vapi)</span>
        </div>
        <span class="exp-date" data-b="text">Apr 2023 – Feb 2024</span>
      </div>
      <ul class="exp-points">
        <li data-b="text">Built RESTful APIs, authentication systems, and responsive UIs using HTML/CSS, JavaScript, Python, Django, PHP, and MongoDB.</li>
        <li data-b="text">Delivered Agile full-stack features including debugging and performance optimisation for scalable web solutions.</li>
      </ul>
      <div class="tags" data-b="box">
        <span>Python</span><span>Django</span><span>JavaScript</span><span>MongoDB</span><span>PHP</span><span>REST APIs</span>
      </div>
    </article>

  </div>
</section>

<!-- ================= PROJECTS ================= -->
<section class="sec" id="work">
  <div data-block>
    <h2 class="h" data-b="text">Featured Projects</h2>
    <p class="sub" data-b="text">Smart contracts, DeFi protocols, enterprise permissioned networks, and AI pipelines.</p>
  </div>
  <div class="cards">

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- Certificate + Hash Anchor + QR scanner line -->
        <rect class="s" x="48" y="28" width="130" height="124" rx="6"/>
        <line class="s" x1="64" y1="48" x2="130" y2="48"/>
        <line class="d" x1="64" y1="62" x2="160" y2="62"/>
        <line class="d" x1="64" y1="74" x2="148" y2="74"/>
        <line class="d" x1="64" y1="86" x2="120" y2="86"/>
        <circle class="a t-zone" cx="150" cy="118" r="14"/>
        <!-- Polygon & Avalanche connected blocks -->
        <rect class="s" x="204" y="38" width="76" height="42" rx="4"/>
        <rect class="s" x="204" y="100" width="76" height="42" rx="4"/>
        <path class="as" d="M178 90h26" stroke-dasharray="4 6" style="animation:dash 1s linear infinite"/>
        <circle class="a" cx="242" cy="59" r="6"/>
        <circle class="a" cx="242" cy="121" r="6"/>
      </svg></div>
      <div class="body">
        <span class="kind" data-b="box">Web3 &bull; Blockchain</span>
        <h3 data-b="text">Academic Credentialing Platform</h3>
        <p data-b="text">Blockchain-based certification platform integrated with university UMS via REST APIs for one-click tamper-proof certificate generation. Solidity contracts anchor hashes on Polygon/Avalanche; zero-registration QR verification portal deployed on AWS (EC2/Lambda/RDS) with Docker and Infura.</p>
        <div class="tags" data-b="box"><span>Solidity</span><span>Polygon</span><span>Avalanche</span><span>AWS</span><span>Docker</span><span>Infura</span></div>
      </div>
    </article>

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- Land registry grid & Merkle Tree Root -->
        <path class="s" d="M40 140 L100 40 L210 50 L270 140 Z"/>
        <line class="d" x1="100" y1="40" x2="155" y2="140"/>
        <line class="d" x1="155" y1="45" x2="210" y2="140"/>
        <line class="d" x1="60" y1="105" x2="245" y2="110"/>
        <!-- Merkle tree radar nodes -->
        <circle class="s" cx="155" cy="45" r="12"/>
        <path class="as t-sweep" d="M155 45L220 120"/>
        <circle class="a t-zone" cx="100" cy="100" r="5"/>
        <circle class="a t-zone" cx="180" cy="95" r="6" style="animation-delay:.6s"/>
        <circle class="a t-zone" cx="230" cy="125" r="5" style="animation-delay:1.2s"/>
      </svg></div>
      <div class="body">
        <span class="kind" data-b="box">Enterprise Blockchain</span>
        <h3 data-b="text">Land Record Verification</h3>
        <p data-b="text">Permissioned blockchain platform for government land records built on Hyperledger Fabric with chaincode functions (Register, Amend, GetHistory, Verify). Merkle-root batch anchoring for historical datasets; Private Data Collections keep sensitive citizen metadata off-chain in compliance with Digital India policies.</p>
        <div class="tags" data-b="box"><span>Hyperledger Fabric</span><span>Chaincode</span><span>Go</span><span>Private Data</span><span>MSP</span></div>
      </div>
    </article>

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- DeFi Vault & Token Lock / Equalizer -->
        <rect class="s" x="50" y="32" width="94" height="116" rx="8"/>
        <circle class="a" cx="97" cy="80" r="20"/>
        <circle class="s" cx="97" cy="80" r="10"/>
        <!-- Token flow to Runes / Ordinals / Stablecoin -->
        <path class="as" d="M144 90h48" stroke-dasharray="4 6" style="animation:dash 1s linear infinite"/>
        <rect class="a t-pk" x="140" y="84" width="12" height="12"/>
        <!-- Equalizer & stats -->
        <g class="a">
          <rect class="t-eq" x="204" y="90" width="10" height="38"/>
          <rect class="t-eq" x="222" y="70" width="10" height="58" style="animation-delay:.2s"/>
          <rect class="t-eq" x="240" y="50" width="10" height="78" style="animation-delay:.4s"/>
          <rect class="t-eq" x="258" y="80" width="10" height="48" style="animation-delay:.6s"/>
        </g>
      </svg></div>
      <div class="body">
        <span class="kind" data-b="box">DeFi &bull; ZkVM</span>
        <h3 data-b="text">BIMA Protocol</h3>
        <p data-b="text">Rust smart contracts on Arch Network (ZkVM/UTXO model) enabling DeFi borrowing, lending, minting, and burning. Developed USBD stablecoin collateral-lock mechanism, integrated BEC20 tokens, Bitcoin Runes & Ordinals, and Bitcoin LST derivatives with decentralized on-chain governance.</p>
        <div class="tags" data-b="box"><span>Rust</span><span>Arch Network</span><span>ZkVM</span><span>Bitcoin Runes</span><span>DeFi</span><span>USBD</span></div>
      </div>
    </article>

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- PKI Two-way mTLS Mutual Authentication Shield -->
        <path class="s" d="M160 26 L236 56 L236 108 C236 142 160 166 160 166 C160 166 84 142 84 108 L84 56 Z"/>
        <!-- X.509 cert lines -->
        <rect class="d" x="116" y="70" width="88" height="8" rx="2"/>
        <rect class="d" x="124" y="86" width="72" height="8" rx="2"/>
        <!-- Lock & Key pulse -->
        <circle class="a t-zone" cx="160" cy="116" r="14"/>
        <circle class="s" cx="160" cy="116" r="6"/>
      </svg></div>
      <div class="body">
        <span class="kind" data-b="box">Cybersecurity &bull; PKI</span>
        <h3 data-b="text">Western Railway Auth System</h3>
        <p data-b="text">Production certificate-based authentication system replacing passwords with X.509 digital certificates. Implemented SSL/TLS mutual authentication (mTLS) for two-way client/server identity verification, automated OpenSSL CA lifecycle with CRL checking, and built secure admin auditing portal.</p>
        <div class="tags" data-b="box"><span>mTLS</span><span>X.509</span><span>OpenSSL</span><span>PKI</span><span>Western Railway</span><span>SSO</span></div>
      </div>
    </article>

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- IPFS Distributed Document Nodes -->
        <polygon class="s" points="160,30 240,75 240,140 160,165 80,140 80,75"/>
        <circle class="a t-zone" cx="160" cy="98" r="16"/>
        <line class="as" x1="80" y1="75" x2="160" y2="98" stroke-dasharray="3 5" style="animation:dash 1.2s linear infinite"/>
        <line class="as" x1="240" y1="75" x2="160" y2="98" stroke-dasharray="3 5" style="animation:dash 1.2s linear infinite"/>
        <line class="as" x1="160" y1="165" x2="160" y2="98" stroke-dasharray="3 5" style="animation:dash 1.2s linear infinite"/>
        <circle class="a" cx="80" cy="75" r="5"/>
        <circle class="a" cx="240" cy="75" r="5"/>
        <circle class="a" cx="160" cy="30" r="5"/>
      </svg></div>
      <div class="body">
        <span class="kind" data-b="box">Storage &bull; Smart Contracts</span>
        <h3 data-b="text">SMP School Management Portal</h3>
        <p data-b="text">Decentralised document storage platform leveraging IPFS as a distributed database with on-chain cryptographic hash anchoring. Guarantees tamper-proof, publicly auditable academic records without reliance on centralized server silos or proprietary single points of failure.</p>
        <div class="tags" data-b="box"><span>IPFS</span><span>Filecoin</span><span>Smart Contracts</span><span>Ethereum</span><span>Web3</span></div>
      </div>
    </article>

    <article class="card" data-block data-b="box">
      <div class="thumb" data-b="box"><svg viewBox="0 0 320 180">
        <!-- AI Brain / Voice Waveform & JARVIS Bot -->
        <rect class="s" x="90" y="40" width="140" height="90" rx="12"/>
        <path class="s" d="M128 130v22h64v-22"/>
        <rect class="a t-eye" x="122" y="65" width="26" height="36" rx="8"/>
        <rect class="a t-eye" x="172" y="65" width="26" height="36" rx="8"/>
        <path class="as" d="M60 85h24M236 85h24" stroke-dasharray="4 6" style="animation:dash 1s linear infinite"/>
      </svg></div>
      <div class="body">
        <span class="kind hw" data-b="box">AI &bull; NLP &bull; Voice</span>
        <h3 data-b="text">Tourism AI & JARVIS Assistant</h3>
        <p data-b="text">Dual AI system: Tourism AI implements machine learning destination recommendation, route optimisation, and a real-time NLP chatbot across all Indian states. JARVIS is a personal AI assistant integrating natural language speech-to-text, schedule automation, and real-time retrieval.</p>
        <div class="tags" data-b="box"><span>Python</span><span>MongoDB</span><span>NLP</span><span>Speech Recognition</span><span>Scikit-learn</span></div>
      </div>
    </article>

  </div>
</section>

<!-- ================= STACK ================= -->
<section class="sec" id="stack">
  <div data-block>
    <h2 class="h" data-b="text">Technical Arsenal</h2>
    <p class="sub" data-b="text">Core languages, smart contract frameworks, and enterprise infrastructure I engineer with.</p>
  </div>
  <div class="stack" data-block>
    <div class="row" data-b="box"><h3 data-b="text">Blockchain & Web3</h3><div class="chips">
      <span class="hot" data-b="box">Solidity</span><span class="hot" data-b="box">Hyperledger Fabric</span><span class="hot" data-b="box">Rust</span><span data-b="box">Go Chaincode</span><span data-b="box">Hardhat</span><span data-b="box">Truffle</span><span data-b="box">IPFS</span><span data-b="box">Filecoin</span><span data-b="box">Ethers.js</span><span data-b="box">Web3.js</span><span data-b="box">Polygon</span><span data-b="box">Avalanche</span><span data-b="box">Arch Network</span><span data-b="box">Merkle Trees</span></div></div>
    
    <div class="row" data-b="box"><h3 data-b="text">Backend & APIs</h3><div class="chips">
      <span class="hot" data-b="box">Node.js</span><span class="hot" data-b="box">Python</span><span data-b="box">Django</span><span data-b="box">PHP</span><span data-b="box">REST APIs</span><span data-b="box">GraphQL</span><span data-b="box">Microservices</span></div></div>

    <div class="row" data-b="box"><h3 data-b="text">Frontend</h3><div class="chips">
      <span class="hot" data-b="box">Next.js</span><span class="hot" data-b="box">React</span><span data-b="box">JavaScript</span><span data-b="box">TypeScript</span><span data-b="box">Tailwind CSS</span><span data-b="box">HTML5</span><span data-b="box">CSS3</span><span data-b="box">Bootstrap</span><span data-b="box">jQuery</span></div></div>

    <div class="row" data-b="box"><h3 data-b="text">AI & Machine Learning</h3><div class="chips">
      <span class="hot" data-b="box">LangChain</span><span data-b="box">Hugging Face</span><span data-b="box">RAG</span><span data-b="box">NLP Pipelines</span><span data-b="box">Scikit-learn</span><span data-b="box">Pandas</span><span data-b="box">NumPy</span><span data-b="box">Prompt Engineering</span></div></div>

    <div class="row" data-b="box"><h3 data-b="text">Databases</h3><div class="chips">
      <span class="hot" data-b="box">MySQL</span><span class="hot" data-b="box">MongoDB</span><span data-b="box">FAISS</span><span data-b="box">Pinecone</span><span data-b="box">IPFS DB</span></div></div>

    <div class="row" data-b="box"><h3 data-b="text">Cloud, DevOps & Security</h3><div class="chips">
      <span class="hot" data-b="box">AWS (EC2/Lambda/S3/RDS)</span><span class="hot" data-b="box">Docker</span><span data-b="box">Git/GitHub</span><span data-b="box">Linux</span><span data-b="box">Postman</span><span data-b="box">mTLS</span><span data-b="box">OpenSSL PKI</span></div></div>
  </div>
</section>

<!-- ================= CREDENTIALS ================= -->
<section class="sec" id="credentials">
  <div data-block>
    <h2 class="h" data-b="text">Education & Honors</h2>
    <p class="sub" data-b="text">Formal academic training, professional certifications, and national cybersecurity recognition.</p>
  </div>
  <div class="cred-grid">

    <div class="cred-card" data-block data-b="box">
      <span class="badge award" data-b="box">National Honor</span>
      <h3 data-b="text">Hack Proof — Ministry of Home Affairs</h3>
      <p data-b="text">Recognised by the Ministry of Home Affairs (MHA), Government of India, for excellence in cybersecurity, vulnerability assessment, and defense.</p>
      <span class="meta" data-b="text">Govt of India &bull; MHA</span>
    </div>

    <div class="cred-card" data-block data-b="box">
      <span class="badge award" data-b="box">Govt Recognition</span>
      <h3 data-b="text">Western Railway Auth System</h3>
      <p data-b="text">Delivered and recognised by Western Railway for designing and deploying a production-grade digital certificate authentication system (mTLS & PKI).</p>
      <span class="meta" data-b="text">Western Railway &bull; S&T Institute</span>
    </div>

    <div class="cred-card" data-block data-b="box">
      <span class="badge" data-b="box">Degree</span>
      <h3 data-b="text">B.Tech in Information Technology</h3>
      <p data-b="text">Aditya Silver Oak Institute of Technology, Ahmedabad. Cumulative GPA: <b>9.10 / 10.0</b>. Focused on distributed systems, blockchain architecture, cryptography, and full-stack software.</p>
      <span class="meta" data-b="text">Expected July 2026 &bull; Silver Oak Univ</span>
    </div>

    <div class="cred-card" data-block data-b="box">
      <span class="badge" data-b="box">Certification</span>
      <h3 data-b="text">Python for Data Science</h3>
      <p data-b="text">NPTEL certification from <b>IIT Madras</b> covering Python data science pipelines, computational statistics, data munging, and machine learning models.</p>
      <span class="meta" data-b="text">NPTEL &bull; IIT Madras</span>
    </div>

    <div class="cred-card" data-block data-b="box">
      <span class="badge" data-b="box">Certification</span>
      <h3 data-b="text">Software Engineering</h3>
      <p data-b="text">NPTEL certification from <b>IIT Kharagpur</b> covering modern software architecture patterns, agile lifecycles, testing methodologies, and system design.</p>
      <span class="meta" data-b="text">NPTEL &bull; IIT Kharagpur</span>
    </div>

    <div class="cred-card" data-block data-b="box">
      <span class="badge" data-b="box">Academics</span>
      <h3 data-b="text">HSC Science</h3>
      <p data-b="text">Dev International School, Junagadh. Higher Secondary Certificate in Science stream with 78% score.</p>
      <span class="meta" data-b="text">March 2022</span>
    </div>

  </div>
</section>

<!-- ================= CONTACT ================= -->
<section class="sec contact" id="contact">
  <div class="swarm-stage" id="swarmStage"></div>
  <div data-block data-finale>
    <h2 class="h" data-b="text">Let's build together</h2>
    <p class="sub" data-b="text">Available for full-time roles, blockchain dApp architecture, DeFi smart contracts, and Web3 consulting.</p>
    <div class="cta">
      <a class="btn pri" data-link="email" href="mailto:sojitrayashkumar@gmail.com" data-b="box">sojitrayashkumar@gmail.com</a>
      <a class="btn" data-link="linkedin" href="https://www.linkedin.com/in/sojitra-yashkumar" target="_blank" rel="noopener" data-b="box">Connect on LinkedIn</a>
      <a class="btn" data-link="github" href="https://github.com/sojitrayash" target="_blank" rel="noopener" data-b="box">View GitHub Repos</a>
      <a class="btn" href="assets/Yash_Sojitra_Resume.pdf" target="_blank" rel="noopener" data-b="box">Download Resume PDF</a>
    </div>
    <p class="foot" data-b="text">This portfolio was assembled live by 18 autonomous agents. Music: <b>Aura Farming</b> (0:00–0:35 looped). Press <kbd>R</kbd> to replay, <kbd>A</kbd> for auto-glide, <kbd>C</kbd> to cycle accent color.</p>
  </div>
</section>

</main>

<!-- tool layer -->
<div id="stage" aria-hidden="true"></div>
<canvas id="swarm" aria-hidden="true"></canvas>
<div class="scan" aria-hidden="true"></div>
<div class="boot" id="boot">
  <div class="chip">YS</div>
  <p id="hint">Press <kbd>Space</kbd> and 18 agents will build this portfolio</p>
</div>

<div class="hud" id="hud">
  <span class="avs" id="avs"></span>
  <span class="hide-s"><span id="nAgents">18</span> agents</span>
  <span><span id="nDone">0</span> / <span id="nAll">0</span> layers</span>
  <span class="bar hide-s"><i id="bar"></i></span>
  <span class="st" id="st">Ready</span>
  <button class="go" id="bTour" title="Start or pause (Space)"><svg viewBox="0 0 12 12" id="icoPlay"><path d="M2 1l9 5-9 5z"/></svg></button>
  <button id="bAuto" class="tog on hide-s" title="Auto-scroll on/off (A)">Auto</button>
  <button id="bSpeed" title="Speed (1 / 2 / 3)">1x</button>
  <button id="bSound" title="Sound (M)"><svg viewBox="0 0 12 12"><path d="M1 4h2.5L7 1v10L3.5 8H1z"/><path d="M8.5 3.5a3.5 3.5 0 010 5" fill="none" stroke="currentColor" stroke-width="1.2"/><path class="mutedline" d="M1 11L11 1" stroke="currentColor" stroke-width="1.4"/></svg></button>
  <button id="bMusic" class="music-pill playing hide-s" title="Aura Farming (First 35s Looped)">
    <span class="music-bars"><i></i><i></i><i></i></span>
    <span class="music-name">Aura Farming</span>
    <span class="music-time" id="musicTime">0:00 / 0:35</span>
  </button>
  <button id="bReplay" title="Replay (R)"><svg viewBox="0 0 12 12"><path d="M6 1.5A4.5 4.5 0 1010.5 6H9a3 3 0 11-3-3v2l3.5-2.75L6 0z"/></svg></button>
</div>

<script>
/* =====================================================================
   SETTINGS — Yash Sojitra Portfolio Configuration
   ===================================================================== */
const CFG = {
  links: {
    github:   'https://github.com/sojitrayash',
    linkedin: 'https://www.linkedin.com/in/sojitra-yashkumar',
    email:    'sojitrayashkumar@gmail.com',
    resume:   'assets/Yash_Sojitra_Resume.pdf'
  },
  photo: 'assets/avatar.png',
  music: 'assets/aura-farming.mp3',
  agents: 18,
  accent: 'yellow',
  finale: ['YASH', 'BLOCKCHAIN', 'WEB3', "LET'S BUILD"],
  autostart: false,
  sound: true
};
/* ===================================================================== */

const ACCENTS = { yellow:'#fff313', red:'#ff3348', mint:'#3dffb0', violet:'#a58bff' };
const HUES = ['#ff6b5e','#ffb02e','#ffe14d','#7dff8f','#35e0c2','#4db8ff','#8f93ff','#d07bff','#ff7ac8'];
const ROLES = ['solidity','chaincode','smart-contracts','nextjs','mtls-pki','zkgov'];
const Q = new URLSearchParams(location.search);
const $ = (s, r=document) => r.querySelector(s), $$ = (s, r=document) => [...r.querySelectorAll(s)];
const clamp = (v,a,b) => Math.max(a, Math.min(b, v));
const rnd = (a=1,b) => b===undefined ? Math.random()*a : a + Math.random()*(b-a);
const ease = k => k<.5 ? 4*k*k*k : 1 - Math.pow(-2*k+2,3)/2;
const root = document.documentElement;
history.scrollRestoration = 'manual';

/* ---------- links ---------- */
for (const a of $$('[data-link]')) {
  const k = a.dataset.link, v = CFG.links[k];
  if (!v) continue;
  a.href = k === 'email' ? 'mailto:' + v : v;
  if (k !== 'email') { a.target = '_blank'; a.rel = 'noopener'; }
}

/* ---------- accent ---------- */
const accentNames = Object.keys(ACCENTS);
let accentName = ACCENTS[Q.get('accent')] ? Q.get('accent') : (ACCENTS[CFG.accent] ? CFG.accent : 'yellow');
const setAccent = hex => root.style.setProperty('--acc', hex);

/* ---------- virtual clock: choreographed runs on this ---------- */
let speed = clamp(parseFloat(Q.get('speed')) || 1, .25, 4), paused = false, vt = 0;
const timers = new Set(), tweens = new Set();
const wait = ms => new Promise(res => timers.add({ t: vt + ms, res }));
const tween = (dur, fn) => new Promise(res => tweens.add({ t0: vt, dur: Math.max(1, dur), fn, res }));

/* ---------- sound and music engine ---------- */
const sfx = {
  ctx: null, on: CFG.sound && !Q.has('mute'), out: null,
  unlock() {
    if (this.ctx) {
      if (this.ctx.state === 'suspended') this.ctx.resume();
    } else {
      try {
        const C = window.AudioContext || window.webkitAudioContext;
        this.ctx = new C();
        this.out = this.ctx.createGain();
        this.out.gain.value = .45;
        this.out.connect(this.ctx.destination);
      } catch (e) {}
    }
    playMusic();
  },
  tone(freq, dur=.13, type='triangle', vol=.06, when=0) {
    if (!this.on || !this.ctx || this.ctx.state !== 'running') return;
    const t = this.ctx.currentTime + when, o = this.ctx.createOscillator(), g = this.ctx.createGain();
    o.type = type; o.frequency.setValueAtTime(freq, t);
    g.gain.setValueAtTime(0, t);
    g.gain.linearRampToValueAtTime(vol, t + .008);
    g.gain.exponentialRampToValueAtTime(.0001, t + dur);
    o.connect(g); g.connect(this.out);
    o.start(t); o.stop(t + dur + .02);
  },
  lastTick: 0,
  tick() { const n = performance.now(); if (n - this.lastTick < 34) return; this.lastTick = n; this.tone(rnd(1700, 2300), .025, 'square', .01); },
  pop(progress) { const scale = [0,2,4,7,9]; const step = Math.floor(progress * 12) + Math.floor(rnd(3)); const semis = scale[step % 5] + 12 * Math.floor(step / 5); this.tone(220 * Math.pow(2, semis / 12), .16, 'triangle', .05); },
  chord() { [0,4,7,12,16].forEach((s, i) => this.tone(330 * Math.pow(2, s / 12), .9, 'triangle', .04, i * .07)); },
  whoosh() { this.tone(180, .5, 'sawtooth', .02); this.tone(90, .6, 'sine', .05); }
};

/* ---------- Background Music (Aura Farming: first 35 seconds looped) ---------- */
const bgMusic = $('#bgMusic');
let musicStarted = false;
let musicMuted = !sfx.on;

bgMusic.addEventListener('timeupdate', () => {
  // Loop strictly at 35 seconds as requested by the user
  if (bgMusic.currentTime >= 35.0) {
    bgMusic.currentTime = 0;
    if (!bgMusic.paused) bgMusic.play().catch(() => {});
  }
  const cur = Math.min(35, Math.floor(bgMusic.currentTime));
  const m = Math.floor(cur / 60);
  const s = String(cur % 60).padStart(2, '0');
  const mt = $('#musicTime');
  if (mt) mt.textContent = `${m}:${s} / 0:35`;
});

bgMusic.addEventListener('ended', () => {
  bgMusic.currentTime = 0;
  if (!bgMusic.paused) bgMusic.play().catch(() => {});
});

function playMusic() {
  if (musicMuted) return;
  if (!musicStarted) {
    musicStarted = true;
    bgMusic.currentTime = 0;
  }
  bgMusic.volume = 0.55;
  const p = bgMusic.play();
  if (p && p.catch) {
    p.then(() => {
      $('#bMusic') && $('#bMusic').classList.add('playing');
      $('#bMusic') && $('#bMusic').classList.remove('muted');
    }).catch(err => {
      console.log('Autoplay deferred pending interaction');
    });
  }
}

function toggleMusic() {
  if (bgMusic.paused || musicMuted) {
    musicMuted = false;
    sfx.on = true;
    sfx.unlock();
    playMusic();
    $('#bSound').classList.remove('off');
    $('#bMusic').classList.add('playing');
    $('#bMusic').classList.remove('muted');
  } else {
    musicMuted = true;
    bgMusic.pause();
    $('#bMusic').classList.remove('playing');
    $('#bMusic').classList.add('muted');
  }
}

/* ---------- geometry ---------- */
const rectOf = el => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
const stage = $('#stage');

/* ---------- agents ---------- */
const ARROW = c => `<svg class="arrow" viewBox="0 0 17 22"><path d="M2 1.5v16l4.4-4 3 7 2.6-1.1-3-6.9h6z" fill="${c}" stroke="#fff" stroke-width="1.3" stroke-linejoin="round"/></svg>`;
const CROSS = `<svg class="cross" viewBox="0 0 18 18"><path d="M9 1v16M1 9h16" stroke="#050506" stroke-width="4.4" stroke-linecap="round"/><path d="M9 1v16M1 9h16" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>`;
const IBEAM = `<svg class="ibeam" viewBox="0 0 18 18"><path d="M5.5 1.5h7M5.5 16.5h7M9 1.5v15" stroke="#050506" stroke-width="4.2" stroke-linecap="round"/><path d="M5.5 1.5h7M5.5 16.5h7M9 1.5v15" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg>`;
const agents = [];
let idleMode = 'orbit';
const orbitCenter = () => ({ x: scrollX + innerWidth / 2, y: scrollY + innerHeight / 2 });

class Agent {
  constructor(i, n) {
    this.i = i; this.n = n; this.color = HUES[i % HUES.length]; this.idle = true;
    this.x = innerWidth / 2 + rnd(-40, 40); this.y = innerHeight / 2 + rnd(-40, 40); this.vx = 0; this.vy = 0;
    this.phase = rnd(Math.PI * 2); this.rad = rnd(.75, 1.25); this.w = rnd(.9, 1.5) * (Math.random() < .5 ? 1 : -1); this.wt = null; this.wUntil = 0;
    const el = this.el = document.createElement('div'); el.className = 'agent'; el.style.color = this.color;
    el.innerHTML = ARROW(this.color) + CROSS + IBEAM + '<span class="ring"></span>' + (ROLES[i % ROLES.length] ? `<label style="background:${this.color}">${ROLES[i % ROLES.length]}</label>` : '');
    stage.appendChild(el);
  }
  mode(m) { this.el.dataset.mode = m; }
  click() { this.el.classList.remove('click'); void this.el.offsetWidth; this.el.classList.add('click'); }
  moveTo(x, y, o = {}) {
    const sx = this.x, sy = this.y, dx = x - sx, dy = y - sy, d = Math.hypot(dx, dy) || 1;
    const dur = o.dur ?? clamp(170 + d * .5, 210, 760);
    const bend = o.straight ? 0 : rnd(-1, 1) * Math.min(140, d * .3);
    const cx = (sx + x) / 2 - dy / d * bend, cy = (sy + y) / 2 + dx / d * bend;
    this.vx = this.vy = 0;
    return tween(dur, k => { const e = ease(k), u = 1 - e; this.x = u * u * sx + 2 * u * e * cx + e * e * x; this.y = u * u * sy + 2 * u * e * cy + e * e * y; });
  }
  drift(dt, t) {
    let tx, ty;
    if (idleMode === 'ring') {
      const b = $('.contact .btn.pri') || $('.contact h2'), r = rectOf(b), a = this.i / this.n * Math.PI * 2 + t * .00035;
      tx = r.x + r.w / 2 + Math.cos(a) * (r.w / 2 + 52) - 4; ty = r.y + r.h / 2 + Math.sin(a) * (r.h / 2 + 30) - 7;
    } else if (idleMode === 'orbit') {
      const c = orbitCenter(), R = Math.min(innerWidth, innerHeight) * .14 * this.rad + 26;
      const a = this.phase + t * .0011 * this.w; tx = c.x + Math.cos(a) * R * (1 + .18 * Math.sin(t * .002 + this.i)); ty = c.y + Math.sin(a) * R;
    } else {
      const out = !this.wt || this.wt.y < scrollY - 40 || this.wt.y > scrollY + innerHeight + 40;
      if (out || t > this.wUntil || Math.hypot(this.wt.x - this.x, this.wt.y - this.y) < 12) {
        this.wt = { x: scrollX + rnd(30, innerWidth - 40), y: scrollY + rnd(70, innerHeight - 110) }; this.wUntil = t + rnd(1400, 3600);
      }
      tx = this.wt.x; ty = this.wt.y;
    }
    const k = idleMode === 'wander' ? 1.5 : 5, max = idleMode === 'wander' ? 520 : idleMode === 'ring' ? 900 : 2200;
    let dvx = (tx - this.x) * k, dvy = (ty - this.y) * k; const m = Math.hypot(dvx, dvy); if (m > max) { dvx *= max / m; dvy *= max / m; }
    const s = Math.min(1, dt * .006); this.vx += (dvx - this.vx) * s; this.vy += (dvy - this.vy) * s;
    this.x += this.vx * dt / 1000; this.y += this.vy * dt / 1000;
  }
  render() { this.el.style.transform = `translate3d(${this.x.toFixed(1)}px,${this.y.toFixed(1)}px,0)`; }
}

/* ---------- job queue ---------- */
const queue = [], waiters = [];
function enqueue(job, at, prefer) {
  if (waiters.length) {
    let bi = 0, bd = Infinity;
    waiters.forEach((w, i) => { const d = prefer === w.a ? -1 : at ? Math.hypot(w.a.x - at.x, w.a.y - at.y) : 0; if (d < bd) { bd = d; bi = i; } });
    waiters.splice(bi, 1)[0].res(job);
  } else queue.push(job);
}
const dispatch = (fn, at, prefer) => new Promise(res => enqueue(async a => { try { await fn(a); } catch (e) { console.error(e); } res(); }, at, prefer));
async function live(a) {
  for (;;) { const job = queue.shift() || await new Promise(res => waiters.push({ a, res })); a.idle = false; await job(a); a.mode('arrow'); a.idle = true; }
}

/* ---------- blocks and layers ---------- */
const itemOf = new Map();
const blocks = $$('[data-block]').map(el => {
  const els = [el, ...$$('[data-b]', el)].filter(x => x.hasAttribute('data-b') && x.closest('[data-block]') === el);
  const items = els.map(e => { const it = { el: e, wire: null }; it.done = new Promise(r => it.finish = r); itemOf.set(e, it); return it; });
  return { el, items, promise: null };
});
for (const it of itemOf.values()) { const p = it.el.parentElement && it.el.parentElement.closest('[data-b]'); it.parent = p ? itemOf.get(p) : null; }
const total = itemOf.size; let done = 0;
$('#nAll').textContent = total;
const hudCount = () => { $('#nDone').textContent = done; $('#bar').style.width = (done / total * 100) + '%'; };
const status = s => $('#st').textContent = s;

function mkWire(r) {
  const w = document.createElement('div'); w.className = 'wire' + (r.w < 46 ? ' sm' : '');
  w.innerHTML = '<u></u><u></u><u></u><u></u><em></em>'; w.style.cssText = `left:${r.x}px;top:${r.y}px;width:0;height:0`; stage.appendChild(w); return w;
}
async function wireJob(a, it) {
  const r = rectOf(it.el);
  await a.moveTo(r.x, r.y); a.mode('cross');
  const w = it.wire = mkWire(r), dim = w.lastChild, sx = a.x, sy = a.y;
  await tween(clamp(150 + Math.hypot(r.w, r.h) * .3, 190, 560), k => {
    const e = ease(k); a.x = sx + r.w * e; a.y = sy + r.h * e;
    w.style.width = r.w * e + 'px'; w.style.height = r.h * e + 'px'; dim.textContent = Math.round(r.w * e) + ' × ' + Math.round(r.h * e);
  });
  sfx.tick(); a.mode('arrow');
}
function splitChars(el) {
  const orig = el.innerHTML, spans = [], tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [];
  while (tw.nextNode()) nodes.push(tw.currentNode);
  for (const n of nodes) { const f = document.createDocumentFragment(); for (const ch of n.textContent) { const s = document.createElement('span'); s.className = 'ch'; s.textContent = ch; f.appendChild(s); spans.push(s); } n.replaceWith(f); }
  return { orig, spans };
}
async function typeIn(el, a) {
  const { orig, spans } = splitChars(el), n = spans.length; el.classList.add('on'); let shown = 0;
  await tween(clamp(n * 15, 170, 980), k => {
    const upto = Math.round(k * n); if (upto <= shown) return;
    for (let i = shown; i < upto; i++) spans[i].classList.add('v'); shown = upto;
    const r = spans[upto - 1].getBoundingClientRect(); if (r.height) { a.x = r.right + scrollX + 2; a.y = r.top + r.height / 2 + scrollY; }
    sfx.tick();
  });
  el.innerHTML = orig;
}
async function resolveJob(a, it) {
  if (it.parent) await it.parent.done;
  const el = it.el, kind = el.dataset.b, r = rectOf(el);
  if (kind === 'text') {
    await a.moveTo(r.x + 3, r.y + Math.min(r.h / 2, 14)); a.mode('ibeam'); it.wire && it.wire.classList.add('edit');
    await typeIn(el, a);
  } else if (kind === 'mega') {
    await a.moveTo(r.x + r.w * rnd(.2, .8), r.y + r.h * .5); a.click(); el.classList.add('on'); sfx.whoosh();
    const t = $('text', el); it.wire && it.wire.classList.add('edit');
    tween(1500, k => t.style.strokeDashoffset = 2400 * (1 - ease(k)));
    await wait(260);
  } else {
    await a.moveTo(r.x + r.w * rnd(.25, .75), r.y + r.h * rnd(.3, .7)); a.click(); el.classList.add('on'); await wait(110);
  }
  if (it.wire) { const w = it.wire; w.classList.add('out'); setTimeout(() => w.remove(), 200); it.wire = null; }
  done++; hudCount(); sfx.pop(done / total); it.finish();
}
function buildBlock(b) {
  if (b.promise) return b.promise;
  return b.promise = (async () => {
    const at = it => { const r = rectOf(it.el); return { x: r.x, y: r.y }; };
    const p1 = []; for (const it of b.items) { p1.push(dispatch(a => wireJob(a, it), at(it))); await wait(38); }
    await Promise.all(p1); await wait(220);
    const p2 = []; for (const it of b.items) { p2.push(dispatch(a => resolveJob(a, it), at(it))); await wait(58); }
    await Promise.all(p2); b.fin = true;
    if (heroBlocks.every(x => x.fin)) ensurePick();
    if (b.el.hasAttribute('data-finale')) finale();
    if (!autoOn && blocks.every(x => x.fin)) { finished = true; status('Done'); setPlayIcon(); }
  })();
}

/* ---------- colour pick ---------- */
async function pickColour() {
  const anchor = rectOf($('.name')), final = accentName, order = accentNames.filter(n => n !== final).slice(0, 2).concat(final);
  const p = document.createElement('div'); p.className = 'picker';
  p.innerHTML = accentNames.map(n => `<i data-n="${n}" style="background:${ACCENTS[n]}"></i>`).join('');
  p.style.left = anchor.x + anchor.w + 18 + 'px'; p.style.top = anchor.y + 6 + 'px'; stage.appendChild(p);
  if (anchor.x + anchor.w + 18 + 160 > innerWidth) { p.style.left = anchor.x + 'px'; p.style.top = anchor.y + anchor.h + 12 + 'px'; }
  await wait(60); p.classList.add('show');
  await dispatch(async a => {
    for (const n of order) {
      const sw = $(`[data-n="${n}"]`, p), r = rectOf(sw);
      await a.moveTo(r.x + r.w / 2, r.y + r.h / 2, { dur: 300 });
      $$('i', p).forEach(i => i.classList.toggle('sel', i === sw)); setAccent(ACCENTS[n]); if (n === final) root.classList.add('inked'); sfx.pop(n === final ? .9 : .4);
      await wait(n === final ? 120 : 330);
    }
    a.click(); sfx.chord(); await wait(420);
  }, { x: anchor.x + anchor.w, y: anchor.y }, agents[2]);
  p.classList.remove('show'); setTimeout(() => p.remove(), 260);
}

/* ---------- tour ---------- */
let started = false, touring = false, finished = false, autoOn = true, resumable = false, tourGen = 0, manualUntil = 0, startedAt = 0, pickP = null;
const heroBlocks = blocks.filter(b => b.el.closest('.hero'));
const ensurePick = () => pickP || (pickP = pickColour());
const maxScroll = () => Math.max(0, root.scrollHeight - innerHeight);
function scrollToY(y, dur, gen) {
  const from = scrollY, to = clamp(y, 0, maxScroll()); if (Math.abs(to - from) < 2) return Promise.resolve();
  return tween(dur, k => { if (gen === tourGen) scrollTo(0, from + (to - from) * ease(k)); });
}
async function tour() {
  const my = ++tourGen, alive = () => my === tourGen; touring = true; setPlayIcon();
  for (let i = 0; i < blocks.length;) {
    const vh = innerHeight, top = rectOf(blocks[i].el).y; let j = i, bottom = top + rectOf(blocks[i].el).h;
    while (j + 1 < blocks.length) { const r = rectOf(blocks[j + 1].el); if (r.y + r.h > top + vh - 62) break; j++; bottom = Math.max(bottom, r.y + r.h); }
    const gh = bottom - top, first = i === 0;
    const target = first ? 0 : gh < vh - 120 ? top - Math.min((vh - 96 - gh) / 2, vh * .16) : top - 24;
    const group = blocks.slice(i, j + 1).filter(b => !b.fin);
    if (group.length) {
      status(first ? 'Building' : 'Touring');
      const dist = Math.abs(target - scrollY), sc = scrollToY(target, clamp(dist * 1.5, 500, 1500), my);
      await wait(first ? 0 : 320); if (!alive()) return;
      const builds = group.map((b, k) => wait(k * 130).then(() => buildBlock(b)));
      const tall = gh > vh - 40 ? sc.then(() => wait(900)).then(() => scrollToY(bottom - vh + 110, 2600, my)) : null;
      await Promise.all([sc, tall, ...builds]); if (!alive()) return;
      if (first) { await ensurePick(); if (!alive()) return; }
      await wait(first ? 950 : 620); if (!alive()) return;
    }
    i = j + 1;
  }
  if (scrollY < maxScroll() - 60) { await scrollToY(maxScroll(), 1300, my); if (!alive()) return; }
  touring = false; finished = true; status('Done'); setPlayIcon();
}
function handsOn(e) {
  if (!started || paused) return;
  if (finished) { if (cruising) { cruising = false; tourGen++; status('Done'); } return; }
  if (e && e.type === 'wheel' && (Math.abs(e.deltaY) < 4 || performance.now() - startedAt < 1200)) return;
  manualUntil = performance.now() + 1700;
  if (touring) { touring = false; tourGen++; status('Manual'); for (const b of visible) buildBlock(b); }
}
function toggleAuto() {
  if (finished) return cruise();
  autoOn = !autoOn; $('#bAuto').classList.toggle('on', autoOn); manualUntil = 0;
  if (!autoOn && touring) { touring = false; tourGen++; for (const b of visible) buildBlock(b); }
  if (started) status(autoOn ? 'Touring' : 'Auto-scroll off');
}
let cruising = false;
async function cruise() {
  const my = ++tourGen; cruising = true; status('Gliding');
  await scrollToY(0, 900, my); await wait(450); if (my !== tourGen) return;
  const d = maxScroll(); await tween(d / .17, k => { if (my === tourGen) scrollTo(0, d * k); });
  if (my === tourGen) { cruising = false; status('Done'); }
}
const visible = new Set();
const io = new IntersectionObserver(es => { for (const e of es) { const b = blocks.find(x => x.el === e.target); e.isIntersecting ? visible.add(b) : visible.delete(b); if (e.isIntersecting && started && !touring) buildBlock(b); } }, { threshold: .12 });
blocks.forEach(b => io.observe(b.el));
addEventListener('wheel', handsOn, { passive: true }); addEventListener('touchmove', handsOn, { passive: true });

/* ---------- finale swarm ---------- */
const swarm = {
  cv: $('#swarm'), ps: [], on: false, mouse: { x: -999, y: -999, t: -9999 }, path: new Path2D('M0 0v15l4.2-3.8 2.8 6.6 2.4-1-2.8-6.5h5.6z'),
  size() { const d = Math.min(2, devicePixelRatio || 1); this.cv.width = innerWidth * d; this.cv.height = innerHeight * d; this.d = d; },
  points(word, n) {
    const r = $('#swarmStage').getBoundingClientRect(), W = Math.round(r.width), H = Math.round(r.height), c = document.createElement('canvas'); c.width = W; c.height = H;
    const x = c.getContext('2d', { willReadFrequently: true }); x.fillStyle = '#fff';
    if (word === '♥') {
      const s = H * .42; x.translate(W / 2, H * .5); x.beginPath();
      for (let t = 0; t <= Math.PI * 2 + .01; t += .05) { const px = 16 * Math.pow(Math.sin(t), 3), py = -(13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t)); x.lineTo(px * s / 16, py * s / 16); }
      x.fill();
    } else {
      let fs = H * 1.04; x.font = `900 ${fs}px "Big Shoulders Display"`; const m = x.measureText(word); if (m.width > W * .9) { fs *= W * .9 / m.width; x.font = `900 ${fs}px "Big Shoulders Display"`; }
      x.textAlign = 'center'; x.textBaseline = 'alphabetic'; const mm = x.measureText(word); x.fillText(word, W / 2, H / 2 + mm.actualBoundingBoxAscent / 2 - 6);
    }
    const data = x.getImageData(0, 0, W, H).data, pts = []; let area = 0;
    for (let py = 0; py < H; py += 2) for (let px = 0; px < W; px += 2) if (data[(py * W + px) * 4 + 3] > 128) area += 4;
    const step = Math.max(2, Math.sqrt(area / n) * .98);
    for (let py = step / 2, row = 0; py < H; py += step, row++) for (let px = row % 2 ? step / 2 : 0; px < W; px += step) if (data[((py | 0) * W + (px | 0)) * 4 + 3] > 128) pts.push([px, py]);
    for (let i = pts.length - 1; i > 0; i--) { const k = Math.floor(Math.random() * (i + 1)); [pts[i], pts[k]] = [pts[k], pts[i]]; }
    const outp = []; for (let i = 0; i < n; i++) { const p = pts[i % Math.max(1, pts.length)] || [W / 2, H / 2]; outp.push([p[0] - 3 + (i >= pts.length ? rnd(-3, 3) : 0), p[1] - 5 + (i >= pts.length ? rnd(-3, 3) : 0)]); } return outp;
  },
  shape(word) { const pts = this.points(word, this.ps.length); this.ps.forEach((p, i) => { p.tx = pts[i][0]; p.ty = pts[i][1]; p.vx += rnd(-420, 420); p.vy += rnd(-420, 420); }); },
  async play(words) {
    this.size(); const n = innerWidth < 700 ? 380 : 760, W = innerWidth, H = innerHeight; this.ps = [];
    for (let i = 0; i < n; i++) {
      const side = Math.floor(rnd(4)), x = side === 0 ? -30 : side === 1 ? W + 30 : rnd(W), y = side === 2 ? -30 : side === 3 ? H + 30 : rnd(H);
      this.ps.push({ x, y, vx: 0, vy: 0, tx: 0, ty: 0, k: rnd(20, 46), c: HUES[i % HUES.length], s: innerWidth < 700 ? rnd(.36, .5) : rnd(.46, .64), ph: rnd(6.28) });
    }
    this.on = true;
    for (let i = 0; i < words.length; i++) { this.shape(words[i]); sfx.whoosh(); if (i === words.length - 1) { await wait(700); sfx.chord(); idleMode = 'ring'; stage.classList.add('ring'); break; } await wait(i === 0 ? 2300 : 1700); }
  },
  step(dt, t) {
    if (!this.on) return; const x = this.cv.getContext('2d'), d = this.d, r = $('#swarmStage').getBoundingClientRect(), h = Math.min(.032, dt / 1000 * Math.max(1, speed * .8));
    x.setTransform(1, 0, 0, 1, 0, 0); x.clearRect(0, 0, this.cv.width, this.cv.height);
    for (const p of this.ps) {
      const tx = r.left + p.tx + Math.sin(t * .002 + p.ph) * 1.6, ty = r.top + p.ty + Math.cos(t * .0017 + p.ph) * 1.6;
      let ax = (tx - p.x) * p.k - p.vx * 8.2, ay = (ty - p.y) * p.k - p.vy * 8.2;
      const mx = p.x - this.mouse.x, my = p.y - this.mouse.y, md = mx * mx + my * my; if (md < 9000 && t - this.mouse.t < 2200) { const f = (9000 - md) * .9 / (Math.sqrt(md) + 1); ax += mx * f; ay += my * f; }
      p.vx += ax * h; p.vy += ay * h; p.x += p.vx * h; p.y += p.vy * h;
      x.setTransform(d * p.s, 0, 0, d * p.s, p.x * d, p.y * d); x.fillStyle = p.c; x.fill(this.path); x.lineWidth = 1.1; x.strokeStyle = 'rgba(255,255,255,.85)'; x.stroke(this.path);
    }
  }
};
let hideT;
addEventListener('pointermove', e => {
  swarm.mouse.x = e.clientX; swarm.mouse.y = e.clientY; swarm.mouse.t = performance.now();
  root.classList.remove('nocursor'); clearTimeout(hideT); if (started) hideT = setTimeout(() => root.classList.add('nocursor'), 1300);
});
addEventListener('resize', () => swarm.size());
let finaleRan = false;
async function finale() { if (finaleRan) return; finaleRan = true; await wait(350); swarm.play(CFG.finale); }

if (CFG.photo) $('#photo').src = CFG.photo;

/* ---------- main loop ---------- */
let last = performance.now();
function frame(now) {
  const dt = Math.min(50, now - last); last = now;
  if (!paused) {
    vt += dt * speed;
    for (const tm of [...timers]) if (vt >= tm.t) { timers.delete(tm); tm.res(); }
    for (const tw of [...tweens]) { const k = Math.min(1, (vt - tw.t0) / tw.dur); tw.fn(k); if (k >= 1) { tweens.delete(tw); tw.res(); } }
    for (const a of agents) if (a.idle) a.drift(dt * Math.min(2, speed), now);
  }
  for (const a of agents) a.render();
  swarm.step(paused ? 0 : dt, now);
  if (resumable && !touring && !finished && !paused && autoOn && now > manualUntil) tour();
  requestAnimationFrame(frame);
}

/* ---------- start / controls ---------- */
const setPlayIcon = () => { const running = started && !paused && !finished; $('#icoPlay').innerHTML = finished ? '<path d="M6 1.5A4.5 4.5 0 1010.5 6H9a3 3 0 11-3-3v2l3.5-2.75L6 0z"/>' : running ? '<path d="M2 1h3v10H2zM7 1h3v10H7z"/>' : '<path d="M2 1l9 5-9 5z"/>'; };
async function start() {
  if (started) return; started = true; startedAt = performance.now(); root.classList.add('nocursor'); sfx.unlock(); root.classList.remove('locked'); scrollTo(0, 0); setPlayIcon();
  status('Scanning page…'); $('#hint').style.opacity = 0; sfx.whoosh();
  const scan = $('.scan'); scan.style.opacity = 1; await tween(820, k => scan.style.transform = `translateY(${ease(k) * innerHeight}px)`); scan.style.opacity = 0;
  idleMode = 'wander'; $('#boot').classList.add('off'); await wait(260);
  resumable = true; if (autoOn) tour(); else for (const b of visible) buildBlock(b);
}
function toggle() { if (finished) return replay(); if (!started) return start(); paused = !paused; if (!paused) sfx.unlock(); status(paused ? 'Paused' : touring ? 'Touring' : autoOn ? 'Manual' : 'Auto-scroll off'); setPlayIcon(); }
function replay() { scrollTo(0, 0); try { sessionStorage.setItem('rp-replay', '1'); } catch (e) {} location.reload(); }
function setSpeed(s) { speed = s; $('#bSpeed').textContent = s + 'x'; }
function toggleSound() {
  sfx.on = !sfx.on;
  if (sfx.on) {
    sfx.unlock();
    musicMuted = false;
    playMusic();
  } else {
    musicMuted = true;
    bgMusic.pause();
  }
  $('#bSound').classList.toggle('off', !sfx.on);
  $('#bMusic').classList.toggle('playing', sfx.on);
  $('#bMusic').classList.toggle('muted', !sfx.on);
}
$('#bTour').onclick = e => { e.stopPropagation(); toggle(); };
$('#bAuto').onclick = e => { e.stopPropagation(); toggleAuto(); };
$('#bSpeed').onclick = e => { e.stopPropagation(); setSpeed(speed >= 2 ? .5 : speed >= 1 ? 2 : 1); };
$('#bSound').onclick = e => { e.stopPropagation(); toggleSound(); };
$('#bMusic').onclick = e => { e.stopPropagation(); toggleMusic(); };
$('#bReplay').onclick = e => { e.stopPropagation(); replay(); };
addEventListener('click', e => { if (!started && !e.target.closest('.hud')) start(); });
addEventListener('pointerdown', () => sfx.ctx && sfx.unlock(), true); addEventListener('keydown', () => sfx.ctx && sfx.unlock(), true);
addEventListener('keydown', e => {
  if (e.metaKey || e.ctrlKey || e.altKey) return; const k = e.key.toLowerCase();
  if (k === ' ') { e.preventDefault(); toggle(); }
  else if (k === 'r') replay();
  else if (k === 'm') toggleSound();
  else if (k === 'a') toggleAuto();
  else if (k === 'h') root.classList.toggle('clean');
  else if (k === '1') setSpeed(1); else if (k === '2') setSpeed(2); else if (k === '3') setSpeed(.5);
  else if (k === 'c') { accentName = accentNames[(accentNames.indexOf(accentName) + 1) % accentNames.length]; setAccent(ACCENTS[accentName]); root.classList.add('inked'); }
  else if (['arrowdown', 'arrowup', 'pagedown', 'pageup', 'home', 'end'].includes(k)) handsOn();
});

/* ---------- boot ---------- */
(async function boot() {
  try { await Promise.all([document.fonts.load('900 100px "Big Shoulders Display"'), document.fonts.load('400 16px "Bricolage Grotesque"')]); await document.fonts.ready; } catch (e) {}
  const svg = $('.mega'), tx = $('text', svg), c = document.createElement('canvas').getContext('2d'); c.font = '900 300px "Big Shoulders Display"';
  const m = c.measureText(tx.textContent), asc = m.actualBoundingBoxAscent || 215, wd = m.width || 1300;
  svg.setAttribute('viewBox', `-3 -3 ${wd + 6} ${asc + 6}`); tx.setAttribute('x', 0); tx.setAttribute('y', asc);

  const n = clamp(parseInt(Q.get('agents')) || CFG.agents, 4, 60); $('#nAgents').textContent = n;
  for (let i = 0; i < n; i++) { const a = new Agent(i, n); agents.push(a); live(a); }
  $('#avs').innerHTML = HUES.slice(0, 5).map(c => `<i style="background:${c}"></i>`).join('');
  $('#bSound').classList.toggle('off', !sfx.on); setSpeed(speed); hudCount(); swarm.size();
  if (matchMedia('(pointer:coarse)').matches) $('#hint').innerHTML = 'Tap and 18 agents will build this portfolio';
  $('#hint').innerHTML = $('#hint').innerHTML.replace('18', n);

  let again = false; try { again = sessionStorage.getItem('rp-replay') === '1'; sessionStorage.removeItem('rp-replay'); } catch (e) {}
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches && !again && !Q.has('auto') && !Q.has('play');
  if (still) {
    started = finished = true; blocks.forEach(b => b.promise = Promise.resolve()); root.classList.remove('locked'); $('#boot').classList.add('off'); setAccent(ACCENTS[accentName]); root.classList.add('inked'); blocks.forEach(b => b.fin = true);
    $$('[data-b]').forEach(e => e.classList.add('on')); tx.style.strokeDashoffset = 0; done = total; hudCount(); status('Built'); idleMode = 'wander'; setPlayIcon();
  }
  requestAnimationFrame(t => { last = t; frame(t); });
  if (!still && (CFG.autostart || again || Q.has('auto') || Q.has('play'))) setTimeout(start, 900);
})();
</script>
</body>
</html>
'''

with open(r'd:\PortFolio\final-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Generated d:\\PortFolio\\final-portfolio\\index.html successfully!')

