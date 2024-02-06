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
  await listProveedor();
  dataTable = $("#datatable-proveedores").DataTable({});

  dataTableIsInitialized = true;
};

const listProveedor = async () => {
  try {
    const response = await fetch("../list_proveedor");
    const data = await response.json();
    let content = "";
    data.proveedores.forEach((proveedores, index) => {
      const tieneCredito = proveedores.credito ? "Si" : "No";
      content += `<tr>
        <td>${index + 1}</td>
        <td>${proveedores.Nombres}</td>
        <td>${proveedores.ruc_proveedor}</td>
        <td>${proveedores.tipo}</td>
        <td>${proveedores.ciudad}</td>
        <td>${proveedores.pais}</td>
        <td>${tieneCredito}</td>
        <td>${proveedores.Telefono}</td>
        <td>
            <a href="../editar_proveedor/${
              proveedores.ruc_proveedor
            }"><button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button></a>
            <a href="../eliminar_proveedor/${
              proveedores.ruc_proveedor
            }"><button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button></a>
            <a href="../mostrar_proveedor/${
              proveedores.ruc_proveedor
            }"><button class='btn btn-sm btn-secondary'><i class='fa-solid fa-binoculars'></i></button></a>
        </td>
      </tr>`;
    });
    tableBody_proveedores.innerHTML = content;
  } catch (ex) {
    alert(ex);
    console.error(
      "La propiedad 'nombre' no existe en la respuesta del servidor."
    );
  }
};
window.addEventListener("load", async () => {
  await initDataTable();
});
