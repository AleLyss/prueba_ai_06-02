let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
  columnDefs: [
    { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7] },
    { orderable: false, targets: [6, 7] },
    { searchable: false, targets: [0, 6, 7] },
  ],
  destroy: true,
};

const initDataTable = async () => {
  if (dataTableIsInitialized) {
    dataTable.destroy();
  }
  await listProducto();
  dataTable = $("#datatable-clientes").DataTable({});

  dataTableIsInitialized = true;
};

const listProducto = async () => {
  try {
    const response = await fetch("../list_cliente");
    const data = await response.json();
    let content = "";
    data.clientes.forEach((clientes, index) => {
      const tieneTelegram = clientes.telegram ? "Si Tiene" : "No Tiene";
      content += `<tr>
          <td>${index + 1}</td>
          <td>${clientes.nombres_apellidos}</td>
          <td>${clientes.telefono}</td>
          <td>${tieneTelegram}</td>
          <td>${clientes.email}</td>
          <td>${clientes.ciudad}</td>
          <td>${clientes.identificacion}</td>
          <td>
            <a href="../editar_cliente/${
              clientes.identificacion
            }"><button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button></a>
            <a href="../eliminar_cliente/${
              clientes.identificacion
            }"><button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button></a>
            <a href="../mostrar_cliente/${
              clientes.identificacion
            }"><button class='btn btn-sm btn-secondary'><i class='fa-solid fa-binoculars'></i></button></a>
          </td>
        </tr>`;
    });
    tableBody_clientes.innerHTML = content;
  } catch (ex) {
    alert(ex);
  }
};
window.addEventListener("load", async () => {
  await initDataTable();
});
