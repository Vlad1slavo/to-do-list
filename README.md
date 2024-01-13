# Todo-list
Service for creating and maintaining to-do lists 


The project reproduces such features as creating, deleting and updating tasks and tags

### Interface:


#### Create task

![Website interface](https://private-user-images.githubusercontent.com/147310033/293579930-d4672fe2-9a94-4a3a-8bf2-fd6acd4167fc.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDUxNjY2NjksIm5iZiI6MTcwNTE2NjM2OSwicGF0aCI6Ii8xNDczMTAwMzMvMjkzNTc5OTMwLWQ0NjcyZmUyLTlhOTQtNGEzYS04YmYyLWZkNmFjZDQxNjdmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDExM1QxNzE5MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NGY3ZmM2YTJkM2Y5ZWYxN2ZmNzA3OGZjYjUyOWFhOGIwYWQyZjkyZjM0ZjUwNmRlNmNjNGRhNzU0NDAzMmNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.C8DBxRK3HTG8ykwbBTD7-40WuaGo_fYzjZEnAVZVy90)

#### Delete tag

![Website interface](https://private-user-images.githubusercontent.com/147310033/293579931-56a1a1aa-7568-45a9-98ec-f8ebae0de45a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDUxNjY2NjksIm5iZiI6MTcwNTE2NjM2OSwicGF0aCI6Ii8xNDczMTAwMzMvMjkzNTc5OTMxLTU2YTFhMWFhLTc1NjgtNDVhOS05OGVjLWY4ZWJhZTBkZTQ1YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDExM1QxNzE5MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xZWY3OGRlMGUwOWI4MWEwYTc2YjAzMTJmOGQ2MTMzMzZmZjFlZTgwMDZmMGFjYjYzNjcwMTY5OWQxNjhhOTQ3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.zZvPJzNCQE5sPyQuxLHhspZdm0lntvUY-VcI-nvklp0)

#### Update task

![Website interface](https://private-user-images.githubusercontent.com/147310033/293579928-26ed0b31-2e93-4058-a476-301bb9957b3e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDUxNjY2NjksIm5iZiI6MTcwNTE2NjM2OSwicGF0aCI6Ii8xNDczMTAwMzMvMjkzNTc5OTI4LTI2ZWQwYjMxLTJlOTMtNDA1OC1hNDc2LTMwMWJiOTk1N2IzZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDExM1QxNzE5MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMDJmNzY5ODg2MGY0ODZhNDc4NWI4OTI2NDc0ZWM4N2ZiMGIwNWJmYTA3ZjUwZWVjMjQ2YmUwYmRlMzdlYjdkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.WxsEy-wt1HPKmfg5NryfrI9JoL6C7wauYlpp3SpSoqM)
