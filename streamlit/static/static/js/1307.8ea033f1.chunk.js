"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[1307],{51307:(t,i,e)=>{e.r(i),e.d(i,{default:()=>c});e(66845);var n=e(62622),a=e(1515);const r=(0,a.Z)("div",{target:"e115fcil2"})((t=>{let{theme:i}=t;return{display:"flex",flexDirection:"row",flexWrap:"wrap",rowGap:i.spacing.lg}}),""),l=(0,a.Z)("div",{target:"e115fcil1"})((()=>({display:"flex",flexDirection:"column",alignItems:"stretch",width:"auto",flexGrow:0})),""),o=(0,a.Z)("div",{target:"e115fcil0"})((t=>{let{theme:i}=t;return{fontFamily:i.genericFonts.bodyFont,fontSize:i.fontSizes.sm,color:i.colors.fadedText60,textAlign:"center",marginTop:i.spacing.xs,wordWrap:"break-word",padding:"0.125rem"}}),"");var d,s=e(40864);!function(t){t[t.OriginalWidth=-1]="OriginalWidth",t[t.ColumnWidth=-2]="ColumnWidth",t[t.AutoWidth=-3]="AutoWidth"}(d||(d={}));const c=(0,n.Z)((function(t){let i,{width:e,isFullScreen:n,element:a,height:c,endpoints:h}=t;const u=a.width;if(u===d.OriginalWidth||u===d.AutoWidth)i=void 0;else if(u===d.ColumnWidth)i=e;else{if(!(u>0))throw Error("Invalid image width: ".concat(u));i=u}const f={};return c&&n?(f.maxHeight=c,f["object-fit"]="contain"):(f.width=i,u===d.AutoWidth&&(f.maxWidth="100%")),(0,s.jsx)(r,{style:{width:e},children:a.imgs.map(((t,i)=>{const e=t;return(0,s.jsxs)(l,{"data-testid":"stImage",children:[(0,s.jsx)("img",{style:f,src:h.buildMediaURL(e.url),alt:i.toString()}),e.caption&&(0,s.jsx)(o,{"data-testid":"stImageCaption",style:f,children:" ".concat(e.caption," ")})]},i)}))})}))}}]);