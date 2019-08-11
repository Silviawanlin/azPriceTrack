function register(){
    var firstname=$('#firstname').val();
    var lastname=$('#lastname').val();
    var password=$('#password').val();
    var phone=$('#phone').val();
    var email=$('#email').val();

    $.ajax({
        url:"firstname="+firstname+"&lastname="+lastname+"&password="+password+"&mobileno="+phone+"&emailid="+email,
        type: 'GET',
        success: function(data){
                    var resp=JSON.parse(data);
                    if(resp.status=="failure")
                    {
                        alert("Register Failed!");
                        alert("Please try Again with different Email Address! ")
                        window.location.replace('/html/registerPage.html');
                    }
                    else{
                        alert("Register Succseeful!");
                        window.location.replace('/login.html');
                    }
                },
        error: alert("Register Failed! Please try Again with different Email Address! "),
    });
}