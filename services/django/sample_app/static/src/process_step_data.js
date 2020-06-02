/*

 */
$(function () {
    let $form = $('#campaign_step');

    $form.on('submit', function () {
        let payload = $form.serialize();

        $.post($form.attr('action'), payload, function (data) {
            console.log(data)
        });

        return false;
    });
});
