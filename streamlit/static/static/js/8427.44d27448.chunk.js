"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[8427],{18427:(e,t,o)=>{o.r(t),o.d(t,{default:()=>b});var r=o(66845),i=o(25621),n=o(69021),s=o(92627),a=o(21e3),d=o(59033),l=o(36989),c=o(1515);const u=(0,c.Z)("button",{target:"elibz2u1"})((e=>{let{theme:t}=e;return{fontSize:t.fontSizes.sm,lineHeight:"1.4rem",color:t.colors.gray60,backgroundColor:t.colors.transparent,border:"none",boxShadow:"none",padding:"0px","&:hover, &:active, &:focus":{border:"none",outline:"none",boxShadow:"none"},"&:hover":{color:t.colors.primary}}}),""),h=(0,c.Z)("div",{target:"elibz2u0"})((e=>{let{theme:t,expanded:o}=e;return{maxHeight:o?"none":t.breakpoints.toast}}),"");var p=o(40864);const b=(0,i.b)((function(e){let{theme:t,body:o,icon:i,width:c}=e;const b=i?"".concat(i,"&ensp;").concat(o):o,g=function(e){if(e.length>114){let t=e.replace(/^(.{114}[^\s]*).*/,"$1");return t.length>114&&(t=t.substring(0,114).split(" ").slice(0,-1).join(" ")),t.trim()}return e}(b),m=b!==g,[x,f]=(0,r.useState)(!m),[y,w]=(0,r.useState)(0),S=(0,r.useCallback)((()=>{f(!x)}),[x]),v=(0,r.useMemo)((()=>function(e,t){const o=(0,s.Iy)(t);return{Body:{props:{"data-testid":"stToast"},style:{width:"288px",marginTop:"8px",borderTopLeftRadius:t.radii.lg,borderTopRightRadius:t.radii.lg,borderBottomLeftRadius:t.radii.lg,borderBottomRightRadius:t.radii.lg,backgroundColor:o?t.colors.gray10:t.colors.gray90,color:t.colors.bodyText,boxShadow:o?"0px 4px 16px rgba(0, 0, 0, 0.16)":"0px 4px 16px rgba(0, 0, 0, 0.7)"}},InnerContainer:{style:{maxHeight:e?"none":"88px",overflow:"hidden",fontSize:t.fontSizes.sm,lineHeight:"1.4rem"}},CloseIcon:{style:{color:t.colors.bodyText,marginRight:"-5px",width:"1.2rem",height:"1.2rem"}}}}(x,t)),[x,t]),k=(0,r.useMemo)((()=>(0,p.jsxs)(p.Fragment,{children:[(0,p.jsx)(h,{expanded:x,children:(0,p.jsx)(a.ZP,{source:x?b:g,allowHTML:!1,isToast:!0})}),m&&(0,p.jsx)(u,{"data-testid":"toastViewButton",className:"toastViewButton",onClick:S,children:x?"view less":"view more"})]})),[m,x,b,g,S]);(0,r.useEffect)((()=>{if(t.inSidebar)return;const e=n.Z.info(k,{overrides:{...v}});return w(e),()=>{n.Z.update(e,{overrides:{Body:{style:{transitionDuration:0}}}}),n.Z.clear(e)}}),[]),(0,r.useEffect)((()=>{n.Z.update(y,{children:k,overrides:{...v}})}),[y,k,v]);const R=(0,p.jsx)(l.Z,{kind:d.h.ERROR,body:"Streamlit API Error: `st.toast` cannot be called directly on the sidebar with `st.sidebar.toast`. See our `st.toast` API [docs](https://docs.streamlit.io/library/api-reference/status/st.toast) for more information.",width:c});return(0,p.jsx)(p.Fragment,{children:t.inSidebar&&R})}))}}]);