/*Form Validation */
(() => {
  "use strict";

  const forms = document.querySelectorAll(".needs-validation");

  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

/*Toast Animations */
document.addEventListener("DOMContentLoaded", (event) => {
  var myToastEl = document.getElementById("myToast");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });
});

/*Ajax Handling for Create User */
function crudUserSubmitForm(event) {
  event.preventDefault();
  form = document.getElementById("userCrudForm");
  first_name = event.srcElement[0].value;
  last_name = event.srcElement[1].value;
  email = event.srcElement[2].value;
  username = event.srcElement[3].value;
  password = event.srcElement[4].value;
  let data = {
    first_name: first_name,
    last_name: last_name,
    email: email,
    username: username,
    password: password,
  };
  form.reset();
  $("#createUserModal").modal("hide");
  var myToastEl = document.getElementById("ajaxToast");
  var toastBody = document.getElementById("ajaxToastBody");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });
  $.ajax({
    url: `/core/users_handle/0`,
    type: "POST",
    data: {
      data: JSON.stringify(data),
    },
    success: function (response) {
      if (response.status == 200) {
        let table = document.getElementById("usersListTable");
        let row = table.insertRow(1);
        row.setAttribute("id", `row_${response.content.id}`);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);
        let cell4 = row.insertCell(3);
        let cell5 = row.insertCell(4);
        let cell6 = row.insertCell(5);

        cell1.innerHTML = response.content.id;
        cell2.innerHTML = `${response.content.first_name} ${response.content.last_name}`;
        cell3.innerHTML = response.content.username;
        cell4.innerHTML = response.content.email;
        cell5.innerHTML = `<span class="badge text-bg-success">Active</span>`;
        cell6.innerHTML = `
        <button type="submit" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#editUserModal"
            onclick="userUpdateFormData(${response.content.id})">Edit</button>
            <button type="submit" class="btn btn-danger" onclick="deleteUser(${response.content.id})">
              Delete
            </button>
        `;
        toastBody.innerHTML = `User Added Succesfully with id ${response.content.id}`;
      } else if (response.status == 202) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      } else if (response.status == 400) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
      toastBody.innerHTML = `Error Occured, ${status}, ${xhr.responseText}`;
    },
  });
  myToast.show();
}

/*Ajax Handling for Delete User */
function deleteUser(id) {
  let deleteRow = document.getElementById(`row_${id}`);
  var myToastEl = document.getElementById("ajaxToast");
  var toastBody = document.getElementById("ajaxToastBody");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });
  $.ajax({
    url: `/core/users_handle/${id}`,
    type: "DELETE",

    success: function (response) {
      if (response.status == 200) {
        deleteRow.remove();
        toastBody.innerHTML = "User Deleted Successfully";
      } else if (response.status == 404) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      } else if (response.status == 400) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
      toastBody.innerHTML = `Error Occured, ${status}, ${xhr.responseText}`;
    },
  });
  myToast.show();
}

/*Ajax Handling for Update User */
// Handle Update Form Dynamic Update
function userUpdateFormData(id) {
  let editForm = document.getElementById("userUpdateCrudForm");
  let editRow = document.getElementById(`row_${id}`);
  data = {
    id: editRow.cells[1].innerText,
    first_name: editRow.cells[1].innerText.split(" ")[0],
    last_name: editRow.cells[1].innerText.split(" ")[1],
    email: editRow.cells[3].innerText,
    is_active: editRow.cells[4].innerText == "Active" ? 1 : 0,
  };
  editForm.elements[0].value = id;
  editForm.elements[1].value = data.first_name;
  editForm.elements[2].value = data.last_name;
  editForm.elements[3].value = data.email;
  editForm.elements[4].value = data.is_active;
  $("#editUserModal").modal("show");
}
// Handle Update Form Submit
function userUpdateForm(event) {
  event.preventDefault();
  var myToastEl = document.getElementById("ajaxToast");
  var toastBody = document.getElementById("ajaxToastBody");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });
  const id = event.srcElement[0].value;
  data = {
    id: id,
    first_name: event.srcElement[1].value,
    last_name: event.srcElement[2].value,
    email: event.srcElement[3].value,
    is_active: event.srcElement[4].value,
  };
  let editRow = document.getElementById(`row_${id}`);

  $("#editUserModal").modal("hide");
  $.ajax({
    url: `/core/users_handle/${id}`,
    type: "PUT",
    dataType: "json",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      if (response.status == 200) {
        editRow.cells[1].innerText = `${response.content.first_name} ${response.content.last_name}`;
        editRow.cells[3].innerText = response.content.email;
        editRow.cells[4].innerHTML = response.content["is_active"]
          ? `<span class="badge text-bg-success">Active</span>`
          : `<span class="badge text-bg-warning">Unactive</span>`;
        toastBody.innerHTML = response.message;
      } else if (response.status == 404) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      } else if (response.status == 400) {
        toastBody.innerHTML = response.message;
        console.error("Error occurred:", response.status, response.message);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
      toastBody.innerHTML = `Error Occured, ${status}, ${xhr.responseText}`;
    },
  });
  myToast.show();
}

/*Theme Toggle */
$(document).ready(() => {
  const body = document.querySelector("body");
  const checkbox = document.getElementById("theme");
  loadTheme();
  checkbox.addEventListener("change", (e) => {
    const currentTheme = e.target.checked;
    updateTheme(currentTheme);
    updateThemeLocalStorage(currentTheme);
  });
  function loadTheme() {
    window.localStorage.getItem("dark")
      ? (checkbox.checked =
          JSON.parse(window.localStorage.dark) == true ? false : true)
      : updateThemeLocalStorage(checkbox.checked);
    updateTheme(!JSON.parse(window.localStorage.dark));
  }
  function updateTheme(currentTheme) {
    body.setAttribute("data-bs-theme", currentTheme ? "light" : "dark");
  }
  function updateThemeLocalStorage(currentTheme) {
    window.localStorage.dark = !currentTheme;
  }
});
