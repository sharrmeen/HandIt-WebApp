(window.__LOADABLE_LOADED_CHUNKS__=window.__LOADABLE_LOADED_CHUNKS__||[]).push([[198],{299:function(e,t,n){"use strict";n.d(t,"d",(function(){return i})),n.d(t,"a",(function(){return s})),n.d(t,"b",(function(){return l})),n.d(t,"c",(function(){return c}));var a=n(26),o=n(49),r=n(10);function i(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>2&&void 0!==arguments[2]?arguments[2]:null,n={pageData:t,pageName:e},i=function(e,t){if(e===r.a)return t.campaignSlug?"?campaignSlug=".concat(encodeURIComponent(t.campaignSlug)):"";return""}(e,arguments.length>1&&void 0!==arguments[1]?arguments[1]:{});return null===t&&(n=fetch("".concat(o.j,"/").concat(e).concat(i)).then((function(e){return e.json()}))),{type:a.h,payload:n}}function s(e){var t=e;return e||(t=fetch(o.e).then((function(e){return e.json()}))),{type:a.b,payload:t}}function l(){return{type:a.e,payload:fetch(o.g).then((function(e){return e.json()}))}}function c(e){return{type:a.f,payload:fetch("".concat(o.h,"/").concat(e)).then((function(e){return e.json()}))}}},362:function(e,t,n){"use strict";n.d(t,"b",(function(){return p})),n.d(t,"a",(function(){return h}));var a=n(0),o=n.n(a),r=n(37),i=n(2),s=n(3),l=n.n(s),c=n(40),d=n(317),u=n.n(d),g=n(33),m=n.n(g);function p(e){var t=e.text,n=e.to,a=e.onClick;return o.a.createElement(E,{to:n,onClick:a},t,o.a.createElement(R,{color:m.a.z500}))}function h(e){var t=e.text,n=e.to,a=e.onClick;return o.a.createElement(_,{target:"_blank",href:n,onClick:a},t,o.a.createElement(R,{color:m.a.z500}))}p.propTypes={text:l.a.string,to:l.a.string,onClick:l.a.func},p.defaultProps={text:"",to:"",onClick:c.default},h.propTypes={text:l.a.string,to:l.a.string,onClick:l.a.func},h.defaultProps={text:"",to:"",onClick:c.default};var f=Object(i.css)(["color:",";"],m.a.z500),b=Object(i.css)(["font-size:1.4rem;"]),y=Object(i.css)(["font-size:2rem;"]),w=Object(i.css)(["line-height:150%;"]),v=Object(i.css)(["line-height:160%;"]),O=Object(i.css)(["height:0.9rem;"]),P=Object(i.css)(["height:1.1rem;"]),I=Object(i.css)(["width:2rem;"]),k=Object(i.css)(["width:2.2rem;"]),C=Object(i.css)(["text-decoration:none;"]),x=Object(i.css)(["display:flex;"]),j=Object(i.css)(["margin-top:0.1rem;"]),L=Object(i.css)(["margin-top:0.3rem;"]),E=Object(i.default)(r.b).withConfig({displayName:"Link__StyledRouterLink",componentId:"sc-1wfk7t1-0"})([""," "," "," "," "," @media (max-width:480px){"," ","}"],f,C,x,y,v,b,w),_=i.default.a.withConfig({displayName:"Link__StyledAnchor",componentId:"sc-1wfk7t1-1"})([""," "," "," "," "," @media (max-width:480px){"," ","}"],f,C,x,y,v,b,w),R=Object(i.default)(u.a).withConfig({displayName:"Link__StyledRightTriangle",componentId:"sc-1wfk7t1-2"})(["> svg{"," "," ","}@media (max-width:480px){> svg{"," "," ","}}"],k,P,L,I,O,j)},365:function(e,t,n){"use strict";n.d(t,"c",(function(){return a})),n.d(t,"d",(function(){return o})),n.d(t,"a",(function(){return r})),n.d(t,"b",(function(){return i}));var a="INR",o="USD",r="domestic",i="fcra"},887:function(e,t,n){"use strict";var a=n(15),o=n.n(a),r=n(0),i=n.n(r),s=n(12),l=n(3),c=n.n(l),d=n(77),u=n.n(d),g=n(1720),m=n(1729),p=n(1730),h=n(1715),f=n(2),b=n(13),y=n.n(b),w=n(109),v=n(321),O=f.default.div.withConfig({displayName:"styles__Container",componentId:"sc-w38jnc-0"})(["margin-bottom:4.8rem;"]),P=(Object(f.default)(w.P).withConfig({displayName:"styles__Para",componentId:"sc-w38jnc-1"})([""," margin-bottom:2rem;&:last-child{margin-bottom:0;}@media (max-width:480px){margin-bottom:1.5rem;}"],v.j),Object(f.default)(w.P).withConfig({displayName:"styles__Bold",componentId:"sc-w38jnc-2"})([""," color:",";font-weight:500;margin-bottom:2rem;@media (max-width:480px){margin-bottom:1.5rem;}"],v.k,y.a.z700),Object(f.default)(w.P).withConfig({displayName:"styles__ParagraphBlack",componentId:"sc-w38jnc-3"})(["font-size:1.6rem;margin-bottom:2rem;color:",";@media (max-width:480px){font-size:1.2rem;line-height:1.4;}"],y.a.z800)),I=function(e){var t=e.lines;return i.a.createElement(C,null,i.a.createElement(O,null,t.map((function(e){return i.a.createElement(x,{key:e},e)}))))};I.propTypes={lines:c.a.arrayOf(c.a.node).isRequired};var k=I,C=f.default.div.withConfig({displayName:"Conditions__ContainerWapper",componentId:"sc-1cbo6di-0"})(["margin:4rem 0 10rem 0;@media (max-width:480px){margin:2rem 0 10rem 0;}"]),x=Object(f.default)(w.P).withConfig({displayName:"Conditions__Paragraph",componentId:"sc-1cbo6di-1"})(["font-size:1.6rem;margin-bottom:2rem;color:",";@media (max-width:480px){font-size:1.2rem;line-height:1.4;}"],y.a.z500),j=k,L=n(1721),E=n(24),_=n.n(E),R=n(770),N=n(48),T=n(411),A=function(e){var t=e.campaignName,n=e.visible,a=e.donationLinks,o=e.adsTrackingInfo,r=function(e,n,a){return function(){Object(N.d)(t,"campaign-page-donate-bar-".concat(n)),Object(N.c)("AddToCart",{content_ids:[t],value:Object(T.d)(n),currency:"INR"}),o.conversionId&&o.donateBarButtons&&o.donateBarButtons[a]&&Object(N.a)(o.conversionId,o.donateBarButtons[a]),window.open(e)}};return i.a.createElement(D,{visible:n},i.a.createElement(u.a,null,i.a.createElement(R.f,null,a.map((function(e,t){var n=e.url,a=e.title,o=e.caption;return i.a.createElement(S,{key:o},i.a.createElement(R.h,null,a),i.a.createElement(R.e,{btnColor:"red",appearance:"outline",onClick:r(n,o,t)},o))})))))};A.propTypes={campaignName:c.a.string.isRequired,visible:c.a.bool,donationLinks:c.a.arrayOf(c.a.shape({caption:c.a.string.isRequired,title:c.a.string.isRequired,url:c.a.string.isRequired})).isRequired,adsTrackingInfo:c.a.objectOf(c.a.string)},A.defaultProps={visible:!1,adsTrackingInfo:{}};var q=A,D=f.default.div.withConfig({displayName:"DonateBar__Container",componentId:"sc-1u4zb47-0"})(["position:fixed;bottom:0;width:100%;background-color:",";box-shadow:0 1.6rem 6.4rem rgba(28,28,28,0.08);transition:opacity 0.3s;opacity:",";z-index:",";padding-top:2rem;"],_.a,(function(e){return e.visible?1:0}),(function(e){return e.visible?3:0})),S=Object(f.default)(R.g).withConfig({displayName:"DonateBar__StyledDonateButtonSection",componentId:"sc-1u4zb47-1"})(["margin-bottom:2.4rem;@media (max-width:480px){:nth-child(1),:nth-child(2){display:none;}}"]),B=n(951),z=n(1717),U=n(1722),F=n(1716),H=n(1723),M=n(584),G=n(256),W=function(e){var t=e.campaignName,n=e.noIndex,a=e.isClosed,l=e.seoTitle,c=e.seoDescription,d=e.ogTitle,f=e.ogDescription,b=e.ogUrl,y=e.ogImage,w=e.adsTrackingInfo,v=e.noticeAtTop,I=e.bannerImage,k=e.bannerImageMob,C=e.title,x=e.subtitle,E=e.donationLine1,_=e.donationLine2,R=e.donationGoal,T=e.hasFormulaBasedGoal,A=e.showDonationProgress,D=e.donationProgress,S=e.donationLinks,W=e.donationPartnerLogo,Y=e.donationPartnerLogoWidth,K=e.donationPartnerLogoHeight,V=e.donationPartnerLogoWidthMobile,J=e.donationPartnerLogoHeightMobile,Q=e.showPartnerLogoInBanner,X=e.showGoalAndLogoAboveDonateSection,Z=e.hasMonetaryGoal,$=e.curAmountFormatted,ee=e.goalAmountFormatted,te=e.keyPartnersTitle,ne=e.partnerLogos,ae=e.partnerLogoHeight,oe=e.ngoPartnersTitle,re=e.ngoPartnerLogos,ie=e.introParagraphs,se=e.introParagraphsFullWidth,le=e.introImage,ce=e.introImageMob,de=e.introImageWidth,ue=e.introImageHeight,ge=e.introNode,me=e.donationsUse,pe=e.partnerDonationsUse,he=e.partnerDonationsUseTitle,fe=e.conditions,be=e.tracking,ye=e.credits,we=e.usageGalleryTitle,ve=e.showUsageGalleryAtBottom,Oe=e.donationsUseTitle,Pe=e.donationsUseInfographic,Ie=e.donationsUseInfographicHeader,ke=e.donationsCompletedProps,Ce=e.donationsUseImages,xe=e.validationPartners,je=e.tweetIds,Le=e.hasNewPaymentsFlow,Ee=e.disableSubscriptions,_e=e.disableDonateCardSubtitle,Re=e.hiddenDonateBar,Ne=e.singlePaymentLinkPrimary,Te=e.singlePaymentLinkAlternate,Ae=e.leadershipTitle,qe=e.leadershipSubtext,De=e.leadershipImages,Se=Object(s.h)().hash,Be=Object(r.useRef)(),ze=Object(r.useState)(!1),Ue=o()(ze,2),Fe=Ue[0],He=Ue[1],Me=function(e){return a&&ke.report?(Object(N.d)(t,"campaign-page-top-banner-view-report"),void window.open(ke.report,"_blank")):a||!Le?!a&&Re&&Ne?(Object(N.d)(t,"campaign-page-top-banner-donate-now"),void window.open(Ne,"_blank")):void(Be&&Be.current&&e&&(be.donateNowInBanner&&Object(N.b)(be.donateNowInBanner),Object(N.d)(t,a?"campaign-page-top-banner-read-more":"campaign-page-top-banner-donate-now"),a||Object(N.c)("InitiateCheckout",{content_ids:[t]}),w.conversionId&&w.topBannerCTA&&Object(N.a)(w.conversionId,w.topBannerCTA))):void 0};Object(r.useEffect)((function(){"#donate-section"===Se&&void 0!==C&&Me()}),[Se,C]);var Ge=S.map((function(e){return{oneTime:{inr:e.amount,usd:e.usd_amount},recurring:{inr:e.recurring_amount_inr,usd:e.recurring_amount_usd}}}));return i.a.createElement(i.a.Fragment,null,i.a.createElement(G.a,{title:l,description:c,ogTitle:d,ogUrl:b,ogDescription:f,ogImage:y,isNoIndex:n}),i.a.createElement(L.a,{isCampaignClosed:a,hasReport:!!ke.report,bannerImage:I,bannerImageMob:k,title:C,subtitle:x,hasNewPaymentsFlow:Le,disableSubscriptions:Ee,disableDonateCardSubtitle:_e,onDonateClick:Me,singlePaymentLinkAlternate:Te,isClosed:a,hiddenDonateBar:Re,partnerLogo:W,partnerLogoWidth:Y,partnerLogoHeight:K,partnerLogoWidthMobile:V,partnerLogoHeightMobile:J,showPartnerLogo:Q,campaignName:t,donationAmountOptions:Ge}),v&&i.a.createElement(u.a,null,v),!a&&i.a.createElement(M.b,{ref:Be},i.a.createElement(m.a,{campaignName:t,onLeaveViewport:function(){return He(!0)},onEnterViewport:function(){return He(!1)},donationLine1:E,donationLine2:_,donationGoal:R,hasFormulaBasedGoal:T,showDonationProgress:A,donationProgress:D,donationLinks:S,donationPartnerLogo:W,donationPartnerLogoWidth:Y,donationPartnerLogoHeight:K,showGoalAndLogoAbove:X,adsTrackingInfo:w,hideDonationLinks:Re,hasMonetaryGoal:Z,curAmountFormatted:$,goalAmountFormatted:ee})),i.a.createElement(u.a,null,ge||i.a.createElement(g.a,{introParagraphs:ie,introParagraphsFullWidth:se,introImage:le,introImageMob:ce,introImageWidth:de,introImageHeight:ue})),a&&i.a.createElement(M.b,{ref:Be},i.a.createElement(p.a,{thankYouLine1:ke.thankYouLine1,thankYouLine2:ke.thankYouLine2,infographic:ke.infographic})),ne.length>0&&i.a.createElement(z.a,{mobileArrowHidden:!1,tabArrowHidden:!1,arrowHidden:!1,showDots:!1,titleFirstPart:"Our",titleSecondPart:te||"key partners",logos:ne,imagesHeight:ae||"10rem"}),i.a.createElement(h.a,{isClosed:a,lines:me,images:Ce,partnerUseTitle:he,partnerUse:pe,galleryTitle:we,showGalleryAtBottom:ve,donationsUseTitle:Oe,infographic:Pe,infographicHeader:Ie}),i.a.createElement(u.a,null,xe.length>0&&i.a.createElement(U.a,{partners:xe})),re.length>0&&i.a.createElement(B.a,{mobileArrowHidden:!1,tabArrowHidden:!1,arrowHidden:!1,showDots:!1,titleFirstPart:"Our",titleSecondPart:oe||"NGO Partners",logos:re,imagesHeight:ae||"10rem"}),De.length>0&&i.a.createElement(H.a,{title:Ae,subHeadingText:qe,leadershipData:De}),i.a.createElement(u.a,null,je.length>0&&i.a.createElement(F.a,{tweetIds:je}),i.a.createElement(j,{lines:fe}),ye&&i.a.createElement(O,null,i.a.createElement(P,null,ye))),!Re&&i.a.createElement(q,{campaignName:t,visible:Fe,donationLinks:S,adsTrackingInfo:w}))};W.propTypes={campaignName:c.a.string.isRequired,isClosed:c.a.bool,noIndex:c.a.bool,seoTitle:c.a.string.isRequired,seoDescription:c.a.string.isRequired,ogTitle:c.a.string.isRequired,ogDescription:c.a.string.isRequired,ogUrl:c.a.string.isRequired,ogImage:c.a.string.isRequired,adsTrackingInfo:c.a.objectOf(c.a.string),bannerImage:c.a.string.isRequired,bannerImageMob:c.a.string.isRequired,title:c.a.node.isRequired,subtitle:c.a.node.isRequired,noticeAtTop:c.a.node,donationLine1:c.a.node.isRequired,donationLine2:c.a.node,donationGoal:c.a.node.isRequired,showDonationProgress:c.a.bool.isRequired,hasFormulaBasedGoal:c.a.bool,donationProgress:c.a.number,donationLinks:c.a.arrayOf(c.a.shape({caption:c.a.string.isRequired,title:c.a.string.isRequired,url:c.a.string.isRequired})).isRequired,donationPartnerLogo:c.a.string,donationPartnerLogoWidth:c.a.string,donationPartnerLogoHeight:c.a.string,showGoalAndLogoAboveDonateSection:c.a.bool,donationPartnerLogoWidthMobile:c.a.string,donationPartnerLogoHeightMobile:c.a.string,showPartnerLogoInBanner:c.a.bool,keyPartnersTitle:c.a.string,partnerLogos:c.a.arrayOf(c.a.shape({src:c.a.string.isRequired,alt:c.a.string.isRequired})),partnerLogoHeight:c.a.string,ngoPartnersTitle:c.a.string,ngoPartnerLogos:c.a.arrayOf(c.a.shape({src:c.a.string.isRequired,alt:c.a.string.isRequired})),introParagraphs:c.a.arrayOf(c.a.node),introParagraphsFullWidth:c.a.arrayOf(c.a.node),introImage:c.a.string,introImageMob:c.a.string,introImageWidth:c.a.string,introImageHeight:c.a.string,introNode:c.a.node,donationsUse:c.a.arrayOf(c.a.node).isRequired,partnerDonationsUse:c.a.arrayOf(c.a.node),partnerDonationsUseTitle:c.a.node,conditions:c.a.arrayOf(c.a.node).isRequired,tracking:c.a.shape({donateNowInBanner:c.a.string}),credits:c.a.node,usageGalleryTitle:c.a.node,showUsageGalleryAtBottom:c.a.bool,donationsUseTitle:c.a.node,donationsUseInfographic:c.a.string,donationsUseInfographicHeader:c.a.node,donationsCompletedProps:c.a.shape({thankYouLine1:c.a.string,thankYouLine2:c.a.string,infographic:c.a.string,report:c.a.string}),donationsUseImages:c.a.arrayOf(c.a.shape({url:c.a.string,caption:c.a.string,alt:c.a.string})),validationPartners:c.a.arrayOf(c.a.shape({title:c.a.string,description:c.a.node,logo:c.a.string,alt:c.a.string,url:c.a.string,logoWidth:c.a.string,logoHeight:c.a.string})),tweetIds:c.a.arrayOf(c.a.arrayOf(c.a.string)),hasNewPaymentsFlow:c.a.bool,disableSubscriptions:c.a.bool,disableDonateCardSubtitle:c.a.bool,hiddenDonateBar:c.a.bool,singlePaymentLinkPrimary:c.a.string,singlePaymentLinkAlternate:c.a.string,hasMonetaryGoal:c.a.bool,curAmountFormatted:c.a.string,goalAmountFormatted:c.a.string,leadershipTitle:c.a.string,leadershipSubtext:c.a.string,leadershipImages:c.a.arrayOf(c.a.object)},W.defaultProps={isClosed:!1,noIndex:!1,donationLine2:"",donationProgress:0,donationPartnerLogo:"",donationPartnerLogoWidth:"",donationPartnerLogoHeight:"",showGoalAndLogoAboveDonateSection:!1,donationPartnerLogoWidthMobile:"",donationPartnerLogoHeightMobile:"",showPartnerLogoInBanner:!1,hasFormulaBasedGoal:!1,keyPartnersTitle:"key partners",partnerLogos:[],ngoPartnersTitle:"NGO Partners",ngoPartnerLogos:[],partnerLogoHeight:"",introParagraphs:[],introParagraphsFullWidth:[],introImage:"",introImageMob:"",introImageWidth:"",introImageHeight:"",introNode:"",tracking:{},credits:null,donationsCompletedProps:{},donationsUseImages:[],validationPartners:[],tweetIds:[],adsTrackingInfo:{},noticeAtTop:null,hasNewPaymentsFlow:!1,disableSubscriptions:!1,disableDonateCardSubtitle:!1,hiddenDonateBar:!1,singlePaymentLinkPrimary:"",singlePaymentLinkAlternate:"",hasMonetaryGoal:!1,curAmountFormatted:"",goalAmountFormatted:"",partnerDonationsUse:[],partnerDonationsUseTitle:"",leadershipTitle:"",leadershipSubtext:"",leadershipImages:[],showUsageGalleryAtBottom:!1,donationsUseTitle:"",donationsUseInfographic:"",donationsUseInfographicHeader:"",usageGalleryTitle:""};t.a=W},933:function(e,t,n){"use strict";n.d(t,"a",(function(){return b}));var a=n(15),o=n.n(a),r=n(0),i=n.n(r),s=n(3),l=n.n(s),c=n(2),d=n(110),u=n.n(d),g=n(13),m=n.n(g),p=n(934),h=n(477),f="Other";function b(e){var t=e.currency,n=e.amounts,a=e.hasCustom,s=e.onChange,l=e.amount,c=e.selectedIndex,d=e.setSelection,g=e.paymentType,m=e.campaignName,b=void 0===m?"":m,w=e.currencyCode,v=n.map((function(e){return{text:"".concat(t," ").concat(e),value:e}})).concat(a?[{text:f,value:0}]:[]),O=Object(p.a)(v,2),P=O.length-1,C=O[P].length-1,x=c[0]===P&&c[1]===C,j=Object(r.useState)(x?l:""),L=o()(j,2),E=L[0],_=L[1],R=Object(r.useState)(null),N=o()(R,2),T=N[0],A=N[1],q=function(e,n){return function(){_(""),A(""),d([e,n]),s(O[e][n].value,t);var a=e===P&&n===C?"custom-amount-selector":"amount-selector-".concat(O[e][n].value,"-").concat(w);Object(h.d)(b,a)}};Object(r.useEffect)((function(){x||q(c[0],c[1])()}),[t,g]);var D=function(e){var n=e.match(/\d+\.?\d{0,2}/),a=n?n[0]:"",o=Number(a),r=Number.isNaN(o)||0===o;_(a||""),r?(A("Please enter a valid amount"),s(0,t)):(A(null),s(o,t))};return i.a.createElement(I,null,O.map((function(e,n){return i.a.createElement(u.a,{gap:10,key:n},e.map((function(e,a){return i.a.createElement(u.a.Item,{colD:6,colM:6,key:e.text||""},e.text===f?i.a.createElement(y,{value:E,onChange:D,label:f,errorMsg:T||"",currency:t,onClick:q(n,a),selected:c[0]===n&&c[1]===a}):i.a.createElement(k,{selected:c[0]===n&&c[1]===a,onClick:q(n,a),decreaseSize:"feedingindia-campaign"===b},"feedingindia-campaign"===b?i.a.createElement("div",null,"USD"===w?Math.ceil(5.33*e.value):Math.ceil(e.value/15)," ","meals"):i.a.createElement(i.a.Fragment,null),e.text))})))})))}function y(e){var t=e.value,n=e.onChange,a=e.label,o=e.errorMsg,s=e.currency,l=e.onClick,c=e.selected,d=Object(r.useRef)();Object(r.useEffect)((function(){d.current&&c&&d.current.focus()}),[d.current,c]);return i.a.createElement(i.a.Fragment,null,i.a.createElement(k,{onClick:l,hide:c},a),i.a.createElement(w,{hide:!c},i.a.createElement(v,{type:"text",value:t,onChange:function(e){n(e.target.value)},placeholder:"Amount",ref:d}),i.a.createElement(O,null,s),!!o&&i.a.createElement(P,null,o)))}b.propTypes={currency:l.a.string.isRequired,amounts:l.a.arrayOf(l.a.number).isRequired,hasCustom:l.a.bool.isRequired,onChange:l.a.func.isRequired,amount:l.a.number.isRequired,selectedIndex:l.a.arrayOf(l.a.number).isRequired,setSelection:l.a.func.isRequired,paymentType:l.a.string.isRequired,campaignName:l.a.string.isRequired,currencyCode:l.a.string.isRequired},y.propTypes={value:l.a.number.isRequired,onChange:l.a.func.isRequired,label:l.a.string.isRequired,errorMsg:l.a.string.isRequired,currency:l.a.string.isRequired,onClick:l.a.func.isRequired,selected:l.a.bool.isRequired};var w=c.default.div.withConfig({displayName:"AmountSelector__CustomInputWrapper",componentId:"sc-1o589zt-0"})(["margin-top:10px;position:relative;display:",";"],(function(e){return e.hide?"none":"block"})),v=c.default.input.withConfig({displayName:"AmountSelector__AmountInput",componentId:"sc-1o589zt-1"})(["position:relative;width:150px;height:60px;color:#4f4f4f;border:1px #ef4f5f solid;font-size:1.5rem;line-height:2rem;padding:5px;padding-left:35px;border-radius:1.2rem;max-width:100%;@media (max-width:760px){width:100%;}"]),O=c.default.div.withConfig({displayName:"AmountSelector__CurrencyLabel",componentId:"sc-1o589zt-2"})(["position:absolute;display:block;font-weight:500;color:#4f4f4f;font-size:1.5rem;left:15px;top:50%;height:48px;width:20px;line-height:2rem;transform:translateY(-20%);"]),P=c.default.div.withConfig({displayName:"AmountSelector__ErrorText",componentId:"sc-1o589zt-3"})(["position:absolute;left:0;top:100%;padding-top:5px;font-size:10px;line-height:15px;height:15px;color:#ef4f5f;"]),I=c.default.div.withConfig({displayName:"AmountSelector__AmountWrapper",componentId:"sc-1o589zt-4"})(["padding:0;margin-top:1rem;margin-bottom:1rem;"]),k=c.default.button.withConfig({displayName:"AmountSelector__AmountButton",componentId:"sc-1o589zt-5"})(["background:",";display:",";align-items:center;justify-content:center;width:150px;height:60px;font-size:",";line-height:2rem;font-weight:500;color:",";border:1px "," solid;border-radius:1.2rem;margin-top:10px;cursor:pointer;max-width:100%;@media (max-width:760px){width:100%;}&:hover{border-color:#ef4f5f;}"],(function(e){return e.selected?"#EF4F5F":"#fff"}),(function(e){return e.hide?"none":"initial"}),(function(e){return e.decreaseSize?"1.3rem":"2rem"}),(function(e){return e.selected?"#fff":"".concat(m.a.z500)}),(function(e){return e.selected?"#EF4F5F":"#B8B8B8"}))},943:function(e,t,n){"use strict";n.d(t,"a",(function(){return m}));var a=n(0),o=n.n(a),r=n(2),i=n(3),s=n.n(i),l=n(40),c=n(944),d=n.n(c),u=n(13),g=n.n(u);function m(e){var t=e.text,n=e.onClick;return o.a.createElement(L,{onClick:n,href:"#!"},o.a.createElement(E,{color:g.a.z900}),t)}function p(e){var t=e.text,n=e.to;return o.a.createElement(L,{target:"_blank",href:n},t)}m.propTypes={text:s.a.string,onClick:s.a.func},m.defaultProps={text:"",onClick:l.default},p.propTypes={text:s.a.string,to:s.a.string},p.defaultProps={text:"",to:""};var h=Object(r.css)(["color:",";"],g.a.z900),f=Object(r.css)(["font-size:1.4rem;"]),b=Object(r.css)(["font-size:2rem;"]),y=Object(r.css)(["line-height:150%;"]),w=Object(r.css)(["line-height:160%;"]),v=Object(r.css)(["height:0.9rem;"]),O=Object(r.css)(["height:1.1rem;"]),P=Object(r.css)(["width:2rem;"]),I=Object(r.css)(["width:2.2rem;"]),k=Object(r.css)(["text-decoration:none;"]),C=Object(r.css)(["display:flex;"]),x=Object(r.css)(["margin-top:0.1rem;"]),j=Object(r.css)(["margin-top:0.3rem;"]),L=r.default.a.withConfig({displayName:"BackButton__StyledLink",componentId:"sc-7uuw65-0"})([""," "," "," "," "," @media (max-width:480px){"," ","}"],h,k,C,b,w,f,y),E=Object(r.default)(d.a).withConfig({displayName:"BackButton__StyledLeftTriangle",componentId:"sc-7uuw65-1"})(["> svg{"," "," ","}@media (max-width:480px){> svg{"," "," ","}}"],I,O,j,P,v,x)},946:function(e,t,n){"use strict";n.d(t,"a",(function(){return o}));var a=n(26);function o(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"";return{type:a.c,payload:{citizenship:e,source:t}}}},949:function(e,t,n){"use strict";n.d(t,"a",(function(){return o}));var a=n(26);function o(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"";return{type:a.g,payload:{currency:e,source:t}}}},950:function(e,t,n){"use strict";var a=n(8),o=n.n(a),r=n(0),i=n.n(r),s=n(3),l=n.n(s),c=n(76),d=n.n(c),u=n(284),g=n.n(u),m=n(2),p=n(13),h=n.n(p);function f(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function b(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?f(Object(n),!0).forEach((function(t){o()(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):f(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}l.a.string.isRequired;var y=function(e){var t=e.visible,n=e.handleModal,a=e.details,o=e.setDonorDetails,r=e.startPayment,s=e.oldName,l=e.newName;return i.a.createElement(i.a.Fragment,null,i.a.createElement(g.a,{visible:t,onClose:n,showCloseIcon:!0,isCentered:!0,type:"medium"},i.a.createElement(v,null,"As per PAN details, donor's name has been updated from"," ",i.a.createElement("b",null,"'",s,"'")," to ",i.a.createElement("b",null,"'",l,"'")),i.a.createElement(w,null,i.a.createElement(d.a,{onClick:function(){o(b(b({},a),{},{name:l})),n(),r()}},"Update name"))))};t.a=y,y.propTypes={visible:l.a.bool.isRequired,handleModal:l.a.func.isRequired,details:l.a.objectOf(l.a.string).isRequired,setDonorDetails:l.a.func.isRequired,startPayment:l.a.func.isRequired,oldName:l.a.string.isRequired,newName:l.a.string.isRequired};m.default.span.withConfig({displayName:"AlertModal__Title",componentId:"sc-kb421g-0"})(["font-size:2.3rem;font-weight:700;"]);var w=m.default.div.withConfig({displayName:"AlertModal__CreateButtonWrapper",componentId:"sc-kb421g-1"})(["margin:0 2rem 2rem 2rem;padding:0 2rem;display:flex;justify-content:center;"]),v=m.default.div.withConfig({displayName:"AlertModal__InputWrapper",componentId:"sc-kb421g-2"})(["margin:0.6rem 2rem 2rem 2rem;padding:2rem 2rem 0 2rem;text-align:center;font-size:1.9rem;line-height:3rem;& > b{color:",";}"],h.a.z500)}}]);