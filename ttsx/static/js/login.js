$(function () {


    var $user = $('.name_input');
    var $pwd = $('.pass_input');



    $user.blur(function () {
        if($(this).val()=='')
        {
            $(this).next().html('用户名不能为空').show();
        }
        else
        {
            $(this).next().hide();
        }
    });
    $user.keyup(function () {
        if($(this).val()=='')
        {
            $(this).next().html('用户名不能为空').show();
        }
        else
        {
            $(this).next().hide();
        }
    });



    $pwd.blur(function () {
        if($(this).val()=='')
        {
            $(this).next().html('密码不能为空').show();
        }
        else
        {
            $(this).next().hide();
        }
    });
    $pwd.keyup(function () {
        if($(this).val()=='')
        {
            $(this).next().html('密码不能为空').show();
        }
        else
        {
            $(this).next().hide();
        }
    });

    $('.form_input').submit(function () {
        if($user.val() == '' && $pwd.val() == '')
        {
            alert('账号密码不能为空');
        }
        else
        {
            $('form').prop({'action':"/user/login_submit/"});
        }
    })
});
