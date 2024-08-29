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

  myToast.show();
});

/*Ajax Handling for Create User */
function crudUserSubmitForm(event) {
  event.preventDefault();
  form = document.getElementById("userCrudForm");
  csrf_token = event.target[0].value;
  first_name = event.srcElement[1].value;
  last_name = event.srcElement[2].value;
  email = event.srcElement[3].value;
  username = event.srcElement[4].value;
  password = event.srcElement[5].value;
  let data = {
    first_name: first_name,
    last_name: last_name,
    email: email,
    username: username,
    password: password,
  };
  form.reset();
  $.ajax({
    url: `/core/users_handle/0`,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token,
      data: JSON.stringify(data),
    },
    success: function (response) {
      var myToastEl = document.getElementById("ajaxToast");
      var toastBody = document.getElementById("ajaxToastBody");
      var myToast = new bootstrap.Toast(myToastEl, {
        animation: true,
        autohide: true,
        delay: 5000,
      });
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
        cell2.innerHTML =
          response.content.first_name + response.content.last_name;
        cell3.innerHTML = response.content.username;
        cell4.innerHTML = response.content.email;
        cell5.innerHTML = `<span class="badge text-bg-success">${response.content.is_active}</span>`;
        cell6.innerHTML = `
            <button type="submit" class="btn btn-danger" onclick="deleteUser('${response.content.csrftoken}', ${response.content.id})">
              Delete
            </button>
        `;
        toastBody.innerHTML = `User Added Succesfully with id ${response.content.id}`;
      } else if (response.status == 202) {
        toastBody.innerHTML = response.content;
      }
      myToast.show();
      $("#createUserModal").modal("hide");
    },
    error: function (status, error) {
      var myToastEl = document.getElementById("ajaxToast");
      var toastBody = document.getElementById("ajaxToastBody");
      var myToast = new bootstrap.Toast(myToastEl, {
        animation: true,
        autohide: true,
        delay: 5000,
      });
      toastBody.innerHTML = "Error occurred:" + status + error;
      console.error("Error occurred:", status, error);
      myToast.show();
    },
  });
}

/*Ajax Handling for Delete User */
function deleteUser(csrf, id) {
  let deleteRow = document.getElementById(`row_${id}`);
  $.ajax({
    url: `/core/users_handle/${id}`,
    type: "DELETE",
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", csrf);
    },
    success: function (response) {
      var myToastEl = document.getElementById("ajaxToast");
      var toastBody = document.getElementById("ajaxToastBody");
      var myToast = new bootstrap.Toast(myToastEl, {
        animation: true,
        autohide: true,
        delay: 5000,
      });
      if (response.status == 204) {
        deleteRow.remove();
        toastBody.innerHTML = "User Deleted Successfully";
      } else if ((response.status = 404)) {
        toastBody.innerHTML = `User Not Found with id ${id}`;
        console.error(
          "Error occurred:",
          response.status,
          `User Not Found with id ${id}`
        );
      }
      myToast.show();
    },
    error: function (status, error) {
      console.error("Error occurred:", status, error);
    },
  });
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
