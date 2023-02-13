<template>
  <input placeholder="Filter users by" id="search">
  <input type="button" v-on:click="filteredItems" value="Search">
  <table>
    <thead>
    <th v-for="(row, col) in JSON.parse(JSON.stringify(customers))[0]" v-bind:key="col">
      <a href="#" v-on:click="sortBy(col)" class="active: sortKey == col">
        {{ col }}
      </a>
    </th>
    </thead>
    <tbody>
    <tr v-for="user in customers || filteredItems" v-bind:key="user">
      <td v-for="row in Object.values(user) " v-bind:key="row">{{ row }}</td>
    </tr>
    </tbody>
  </table>
</template>

<script>
const {Client: Client7} = require('elasticsearch')
let auth = 'elastic:changeme';
let port = 9200;
let protocol = 'http';
let hostUrls = [
  'localhost',
];

let hosts = hostUrls.map(function (host) {
  return {
    protocol: protocol,
    host: host,
    port: port,
    auth: auth
  };
});
let client = new Client7({
  hosts: hosts,
});


export default {
  name: "App",
  data: () => ({customers: []}),
  sortKey: "name",
  computed: {
    customerList() {
      return JSON.parse(JSON.stringify(this.customers))
    },
  },
  methods: {
    async getObjects() {
      let arr = [];
      const result = await client.search({
        index: 'sample-index',
      })

      for (let i = 0; i < result.hits.total.value; i++) {
        let document = await client.get({
          index: 'sample-index',
          id: i
        })
        arr.push(document._source)

      }
      this.customers = arr;
    },
    sortBy: function (sortKey) {
      let rev = this.sortKey === sortKey;
      this.sortKey = sortKey
      let arr = JSON.parse(JSON.stringify(this.customers))
      arr.sort(function (a, b) {
        let keyA = a[sortKey];
        let keyB = b[sortKey];
        const isNumeric = n => !!Number(n);
        if (isNumeric(keyA) && isNumeric(keyB)) {
          keyA = +keyA;
          keyB = +keyB;
        }
        if (rev) {
          if (keyA < keyB) return -1;
          if (keyA > keyB) return 1;
          return 0;
        } else {
          if (keyA > keyB) return -1;
          if (keyA < keyB) return 1;
          return 0;
        }
      })
      this.customers = arr;
    },
    filteredItems: function () {
      let search = document.getElementById("search").value;
      let arr = JSON.parse(JSON.stringify(this.customers));
      arr = arr.filter(item => {
        return item["customers_firstname"].toLowerCase().indexOf(search.toLowerCase()) > -1
      })
      this.customers = arr
    }
  },
  mounted() {
    this.getObjects()
  },

}
</script>
