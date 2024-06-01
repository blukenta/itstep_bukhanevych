function submitForm(abc, checkboxId, formId) {
    var checkbox = document.getElementById(checkboxId);
    if (checkbox) {
        checkbox.checked = !checkbox.checked;
        checkbox.value = checkbox.checked ? "on" : "";
        
        var hiddenInput = document.getElementsByName(abc)[0]; 
        if (hiddenInput) {
            hiddenInput.value = checkbox.checked ? "False" :"True";
        }

        var form = document.getElementById(formId);
        if (form) {
            form.submit();
        } else {
            console.error("Form with ID '" + formId + "' not found.");
        }
    } else {
        console.error("Checkbox with ID '" + checkboxId + "' not found.");
    }
}
