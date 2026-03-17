document.querySelectorAll("th").forEach((th) => {
    th.addEventListener("click", () => {
        const table = th.closest("table");
        const tbody = table.querySelector("tbody");
        const rows = Array.from(tbody.querySelectorAll("tr"));
        const index = Array.from(th.parentNode.children).indexOf(th);
        const asc = (th.asc = !th.asc);

        rows.sort((a, b) => {
            const aCol = a.children[index].innerText
                .replace(/\s/g, "")
                .replace("kr", "");
            const bCol = b.children[index].innerText
                .replace(/\s/g, "")
                .replace("kr", "");

            const aVal = isNaN(aCol) ? aCol : parseFloat(aCol);
            const bVal = isNaN(bCol) ? bCol : parseFloat(bCol);

            return (aVal > bVal ? 1 : -1) * (asc ? 1 : -1);
        }).forEach((tr) => tbody.appendChild(tr));
    });
});
