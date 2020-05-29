/*

 */
$(function () {
    let $form = $('#campaign_step');
    let $saveButton = $('#save_step');

    for (let key in jsonObject) {
        //let $field = $form.find('#' + key);
        let $field = $form.find('[name="' + key + '"]');

        if (!$field) {
            return true;
        }

        if (jsonObject.hasOwnProperty(key)) {
            console.log(key + " > " + jsonObject[key])

            if ($field.is(':radio')) {
                $form.find('[value="' + jsonObject[key] + '"]').prop('checked', true);
            } else {
                $field.val(jsonObject[key])
            }
        }
    }

    $saveButton.on('click', function () {
        let payload = $form.serialize();

        $.post($form.attr('action'), payload, function (data) {
            console.log(data)
        });

        return false;
    });
});
