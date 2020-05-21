import '../web_modules/@vaadin/vaadin-grid/vaadin-grid.js';

const template = document.createElement('template');
template.innerHTML = `
<style>
    :host {
        display: block;
        font-family: sans-serif;
        color: darkcyan;
    }
</style>
<div class="table">
    <vaadin-grid>
        <vaadin-grid-column path="name" header="Full Name"></vaadin-grid-column>
        <vaadin-grid-column path="status" header="Status"></vaadin-grid-column>
        <vaadin-grid-column path="origin.name" header="Origin"></vaadin-grid-column>
        <vaadin-grid-column path="location.name" header="Current Location"</vaadin-grid-column>
        <vaadin-grid-column path="visitCount" text-align="end" width="120px" flex-grow="0"></vaadin-grid-column>
    </vaadin-grid>
</div>
`;

class SampleTable extends HTMLElement {
    constructor() {
        super();
        this._shadowRoot = this.attachShadow({ 'mode': 'open' });
        this._shadowRoot.appendChild(template.content.cloneNode(true));

        this.$table = this._shadowRoot.querySelector('vaadin-grid');
    }

    connectedCallback() {
        this._renderTable();
    }

    _renderTable() {
        (async () => {
            let response = await fetch('https://rickandmortyapi.com/api/character/');
            let data = await response.json();
            this.$table.items = data.results;
        })();
    }
}

window.customElements.define('sample-table', SampleTable);
