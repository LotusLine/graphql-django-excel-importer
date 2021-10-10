This project serves the purpose of:

1. Import an CSV file to local database using pandas with the script loaddata.py
2. Render the data in GrapQL API 
3. Use Filters to retrieve exactly the info we want


An example query using filters

´´´
query {
  allProductInfo(country: "Germany") {
    edges{
      node {
        segment
        sales
        product
        country
      }
    }
  }
}
```

Tutorial from:
https://www.youtube.com/watch?v=nPQE5B51DQ8