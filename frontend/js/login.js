function login(){
    var username= $('#username').val();
    var password= $('#password').val();
        // if(username=="" || password=="")
        //     alert("Please enter your Username or Password!");
        // else if(!username.includes("@"||!username.includes(".")))
        //     alert("please enter the the Correct unsername");
    password=md5(password);
    console.log(password);

//     $.ajax({
//         url:"http://helpdesk.sitacorp.com:8080/stdnttraining/userLogin?username=shivakumar.gunti@gmail.com&password=803205ab3f1b9b6fa6990393f5ac6b58",
//         type:'GET',
//         success: function(data){
//                     var resp=JSON.parse(data);
//                     if(resp.status=="failure")
//                         {
//                             alert("Login failed! Please check your email address or your password is correct!");
//                         }
//                     else
//                         {
//                             alert("Welcome!");
//                             window.location.replace('');
//                         }
//                     },
//         error: function(){
//             alert("Login failed! Please check your email address or your password is correct!");
//         },
//     });
}