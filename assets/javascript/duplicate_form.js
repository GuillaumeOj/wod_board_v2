const rootMovementEventListener = htmx.on("click", function(event) { addMovementInRoundFormsetForm(event, 0); });

function duplicateForm(originalForm, formNum, idPrefix, idSuffix) {
  const newForm = originalForm.cloneNode(true);

  return incrementFormIndex(newForm, formNum, idPrefix, idSuffix);
}

function incrementFormIndex(form, formNum, idPrefix, idSuffix) {
  const idRegex = RegExp(`${idPrefix}(\\d{1})${idSuffix}`, "g");

  form.innerHTML = form.innerHTML.replace(idRegex, `${idPrefix}${formNum}${idSuffix}`);

  return form;

}

function updateFormsetTotalForms(formset, addButton, newForm, totalFormsElement, totalFormsValue) {
  formset.insertBefore(newForm, addButton);
  totalFormsElement.setAttribute("value", `${totalFormsValue}`);
}

function addMovementInRoundFormsetForm(event, round_index) {
  event.preventDefault();

  const movementForms = document.querySelectorAll(`.movement-in-round-${round_index}-form`);
  const movementsFormset = document.querySelector(`#movements-in-round-${round_index}`);
  const addMovementFormButton = document.querySelector(`#add-movement-in-round-${round_index}-form`);
  const movementFormsetTotalForms = document.querySelector(`#id_movement_in_round_${round_index}-TOTAL_FORMS`);

  let formNum = movementForms.length - 1;

  formNum++;

  // Duplicate the first form in the formset
  const newMovementForm = duplicateForm(
    movementForms[0],
    formNum,
    `movement_in_round_${round_index}-`,
    ""
  );
  const newFormsetTotalFormsValue = formNum + 1;

  // Insert the new form in the formset and update the value of total forms in the formset
  updateFormsetTotalForms(
    movementsFormset,
    addMovementFormButton,
    newMovementForm,
    movementFormsetTotalForms,
    newFormsetTotalFormsValue
  );
}

function addRoundInWodFormsetForm(event) {
  event.preventDefault();

  const roundForms = document.querySelectorAll(".round-form");
  const formset = document.querySelector("#rounds");
  const addFormButton = document.querySelector("#add-round-form");
  const roundFormsetTotalForms = document.querySelector("#id_round_in_wod-TOTAL_FORMS");

  let formNum = roundForms.length - 1;
  formNum++;

  // Duplicate the first form in the formset
  const newRoundForm = duplicateForm(
    roundForms[0],
    formNum,
    "round_in_wod-",
    "-"
  );

  // Increment round number for each form in movement formset
  ["movement_in_round_", "movements-in-round-", "movement-in-round-"].forEach((prefix) => {
    const regex = RegExp(`${prefix}(\\d{1})`, "g");
    newRoundForm.innerHTML = newRoundForm.innerHTML.replace(regex, `${prefix}${formNum}`);
  });
  newRoundForm.querySelector(`#add-movement-in-round-${formNum}-form`).setAttribute("hx-on", `click: addMovementInRoundFormsetForm(event, ${formNum})`);

  // Increment formset title
  newRoundForm.querySelector(".round-title").innerText = `${formNum + 1}`;

  // Insert the new form in the formset and update the value of total forms in the formset
  updateFormsetTotalForms(formset, addFormButton, newRoundForm, roundFormsetTotalForms, formNum + 1);
}
// function addMovementInRoundFormsetForm(event, round_index) {
//   event.preventDefault();

//   const movementForms = document.querySelectorAll(`.movement-in-round-${round_index}-form`);
//   const movementsFormset = document.querySelector(`#movements-in-round-${round_index}`);
//   const addMovementFormButton = document.querySelector(`#add-movement-in-round-${round_index}-form`);
//   const movementFormsetTotalForms = document.querySelector(`#id_movement_in_round_${round_index}-TOTAL_FORMS`);

//   let formNum = movementForms.length - 1

//   // Duplicate the first form in the formset
//   const newRoundForm = movementForms[0].cloneNode(true);

//   formNum++;

//   // Increment form id for each class and id
//   const roundFormRegex = RegExp(`movement_in_round_${round_index}-(\\d){1}-`, "g");
//   newRoundForm.innerHTML = newRoundForm.innerHTML.replace(roundFormRegex, `round_in_wod-${formNum}-`);

//   // Insert the new form in the formset and update the value of total forms in the formset
//   movementsFormset.insertBefore(newRoundForm, addMovementFormButton);
//   movementFormsetTotalForms.setAttribute("value", `${formNum + 1}`);
// }

// function addRoundInWodFormsetForm(event) {
//   event.preventDefault();

//   const roundForms = document.querySelectorAll(".round-form");
//   const formset = document.querySelector("#rounds");
//   const addFormButton = document.querySelector("#add-round-form");
//   const roundFormsetTotalForms = document.querySelector("#id_round_in_wod-TOTAL_FORMS");

//   let formNum = roundForms.length - 1

//   // Duplicate the first form in the formset
//   const newRoundForm = roundForms[0].cloneNode(true);

//   formNum++;
//   const formsTotalNum = formNum + 1;

//   // Increment round number for each fields of the form
//   const roundFormRegex = RegExp(`round_in_wod-(\\d){1}-`, "g");
//   newRoundForm.innerHTML = newRoundForm.innerHTML.replace(roundFormRegex, `round_in_wod-${formNum}-`);

//   // Increment round number for each form in movement formset
//   let movementInRoundFormRegex = RegExp(`movement_in_round_(\\d){1}-`, "g")
//   newRoundForm.innerHTML = newRoundForm.innerHTML.replace(movementInRoundFormRegex, `movement_in_round_${formNum}-`);
//   movementInRoundFormRegex = RegExp(`movements-in-round-(\\d){1}`, "g")
//   newRoundForm.innerHTML = newRoundForm.innerHTML.replace(movementInRoundFormRegex, `movement-in-round-${formNum}`);
//   movementInRoundFormRegex = RegExp(`movement-in-round-(\\d){1}-`, "g")
//   newRoundForm.innerHTML = newRoundForm.innerHTML.replace(movementInRoundFormRegex, `movement-in-round-${formNum}-`);

//   // Increment formset title
//   newRoundForm.querySelector(".round-title").innerText = `${formsTotalNum}`;

//   // Insert the new form in the formset and update the value of total forms in the formset
//   formset.insertBefore(newRoundForm, addFormButton);
//   roundFormsetTotalForms.setAttribute("value", `${formsTotalNum}`);
// }
