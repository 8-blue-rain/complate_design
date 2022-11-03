
        function add_line(){

            function ad_l(){
                var tr = document.createElement("tr");  //创建tr标签
                var td1 = document.createElement("th"); //创建td标签
                var td2 = document.createElement("td"); //创建td标签
                var td3 = document.createElement("td"); //创建td标签
                var td4 = document.createElement("td"); //创建td标签
                var td5 = document.createElement("td"); //创建td标签
                var td6 = document.createElement("td"); //创建td标签

                var td7 = document.createElement("select"); //创建select标签

                var T_1 = document.createElement("input"); //在前2-4个<td>标签里加 input标签
                var T_2 = document.createElement("input");
                var T_3 = document.createElement("input");

                var T_4 = document.createElement("a");
                var T_4_1 = document.createElement("img");


                var atr1 = document.createAttribute("name"); //给第一个input标签加name属性
                var atr2 = document.createAttribute("type"); //给第一个input标签加type属性

                var atr3 = document.createAttribute("name"); //给第2个input标签加name属性
                var atr4 = document.createAttribute("type"); //给第2个input标签加type属性

                var atr5 = document.createAttribute("name"); //给第3个input标签加type属性
                var atr6 = document.createAttribute("type"); //给第3个input标签加type属性

                var atr7 = document.createAttribute("href");

                var atr8 = document.createAttribute("src");
                var atr9 = document.createAttribute("style");
                //有四条数据  分别是 a b c d


                document.getElementById('t1').appendChild(tr);
                tr.appendChild(td1);
                tr.appendChild(td2);
                tr.appendChild(td3);
                tr.appendChild(td4);
                tr.appendChild(td5);
                tr.appendChild(td6);
                td1.appendChild(td7);

                td2.appendChild(T_1);
                td3.appendChild(T_2);
                td4.appendChild(T_3);
                td5.innerHTML="500";
                td6.appendChild(T_4);
                T_4.appendChild(T_4_1);

                atr1.nodeValue="name1"; //设定属性值
                atr2.nodeValue="text";

                atr3.nodeValue="name2";
                atr4.nodeValue="text";

                atr5.nodeValue="name3";
                atr6.nodeValue="text";

                atr7.nodeValue="/sss";

                atr8.nodeValue="static/x_image.png";
                atr9.nodeValue="high:15px;width:15px";

                T_1.attributes.setNamedItem(atr1); //给第一个input标签添加属性
                T_1.attributes.setNamedItem(atr2); //给第一个input标签加type属性

                T_2.attributes.setNamedItem(atr3);
                T_2.attributes.setNamedItem(atr4);

                T_3.attributes.setNamedItem(atr5);
                T_3.attributes.setNamedItem(atr6);

                T_4.attributes.setNamedItem(atr7);
                T_4_1.attributes.setNamedItem(atr8);
                T_4_1.attributes.setNamedItem(atr9);


                var s = x

                for (i=0;i<=s.length-1;i++) {
                    var td8 = document.createElement("option");
                    td8.innerHTML = s[i];
                    td7.appendChild(td8);
                };

            };


            $.ajax({
                async:false,
                type:"POST",
                url: "/dt_log",
                success: function(log){
                    x = log;
                    ad_l();
                },
                error: function () {
                    console.log();{
                        alert('!!!!')
                    }
                }
            })

        }

