function search(){
    $.ajax({
        url: "",
        type: 'GET',
        success: function(data){
            data = JSON.parse(data);
            console.log(data);
            // var myArr= data.data;
            // var htm=$('#data');
            // for(var i=0;i<myArr.length;i++){
            //     htm += '<tr><td>' + myArr[i].firstname + '</td><td>'
            //             + myArr[i].lastname + '</td><td>'
            //             + myArr[i].fullname+ '</td><td>'
            //             + myArr[i].email+'</td><td>'
            //             + myArr[i].phone+'</td><td>';
            // }
            // htm += '</tbody></table>';
            // $("#data").append(htm);
        }
    });
}