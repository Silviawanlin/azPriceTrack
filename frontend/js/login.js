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
//         url:"192.168.200.2:3000/user/register",
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