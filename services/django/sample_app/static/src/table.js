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
        <vaadin-grid-column path="name.first" header="First name"></vaadin-grid-column>
        <vaadin-grid-column path="name.last" header="Last name"></vaadin-grid-column>
        <vaadin-grid-column path="location.city"></vaadin-grid-column>
        <vaadin-grid-column path="location.team"</vaadin-grid-column>
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
        const users = [
            {
                "name": {
                    "first": "Patrick",
                    "last": "Marleau"
                },
                "location": {
                    "city": "Pittsburgh",
                    "team": "Penguins"
                }
            },
            {
                "name": {
                    "first": "Brent",
                    "last": "Burns"
                },
                "location": {
                    "city": "San Jose",
                    "team": "Sharks"
                }
            },
            {
                "name": {
                    "first": "Brendon",
                    "last": "Dillon"
                },
                "location": {
                    "city": "Washington D.C.",
                    "team": "Capitals"
                }
            }
        ];

        this.$table.items = users;
    }
}

window.customElements.define('sample-table', SampleTable);
