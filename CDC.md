# Cahier des charges
This app needs to track expense of an user day by day. The user needs to enter his expense, select its category and save it. He can filter his criteria time/category to have an overview of his expense. He has access to statistics to know his performance. 

## limitation
for now I will only do it for local user

## Tasks explained:
### expense day by day:
user is presented a form where he enter:
-  date;optional hour
-  the category;subcategory
-  tag
-  comment/description
-  title
-  price 
- select the source account debited

save it,  delete it, update it

### income
similar to expense he can also enter its income


### accounts
he can create accounts from where the money is debited/credited, define it balance.

### categories
user have access to a panel to create a categories. He will enter the name of the category and can select an image to defined it. he has an option to select if it a categorie he will then have to scroll and select the category associated

### tags
tag is used to defined something if it important for work of thing like that. user can create those:
- name
- color
- description

### filters
user can filter 
- expense / income
- date range
- categories
- tag
- price value ?
- name


### overview
the user will have basic information of his situation like expense vs income. graph/stats displaying where (categories) the expenses goes

## need to do
- expense
- time tracking
- filters
- accessible 
- authentication ?
- upload image ?
- graph
- categories/subcategories
- tags


## app look
### overview
![frontpage](images/overview.png)
### filters
![frontpage](images/details-categories.png)
![frontpage](images/details-subcategories.png)
![frontpage](images/filter.png)
### expense
![frontpage](images/create_expense.png)
![frontpage](images/edit_expense.png)
### category creation
should have an intermediate page to manage : category where you create, edit, delete categories 
![frontpage](images/create_category.png)
![frontpage](images/edit_categories.png)
### tag creation
same for tag
![frontpage](images/create_tag.png)

### accounts
### login

## navigation
![frontpage](images/navigation.png)



## DB schema
### categories
- id:int unique
- name:varchar(50)
- subcategory: bool
- parent: int foreign key
- description: varchar(500)
- image: blob
### tag
- id:int unique
- name: varchar(50)
- color: ?
- description: varchar(200)
### expense
- id:int unique
- name: varchar(50)
- date: datetime
- amount: int
- income: bool
- account: int foreign key
- category: int foreign key
- subcat: int foreign key
- tag: int foreign key
- cur: int foreign key
- description: varchar(200)
- image: blob

### accounts
- id: int unique
- holder: int foreign key
- amount: int
### user
- id: int unique
- username: varchar(50)
- password: varchar(50) hash

### currency
- id : int unique
- currency: varchar(3)
- fullname: varchar(50) 

## class diagramm
![frontpage](images/diagram_class.png)

## program architecture


## chart

- line graph: to see the overall fortune

- bar graph, column chart : visualize spending/earning

- pie chart: for difference between spending by categories

- bullet graph: for objective goal (not yet but an idea)


