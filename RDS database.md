## How to create a RDS database in AWS and to access it through MySQL workbench ##

### Step 1: Create a RDS database 

In the left navigation pane, research or click (if used before) in RDS. 
Follow these step following:
```{r}
Database/ Create database/ Standard creation/ MySQL/ Freetier
```

Output of each step
![12](https://user-images.githubusercontent.com/51121757/70648851-df1fa100-1c43-11ea-8c4a-77bf41773551.PNG)
![13](https://user-images.githubusercontent.com/51121757/70649046-476e8280-1c44-11ea-9456-748d0525fd97.PNG)
![10](https://user-images.githubusercontent.com/51121757/70648100-45a3bf80-1c42-11ea-8e5a-6984fb620f5a.PNG)
![11](https://user-images.githubusercontent.com/51121757/70648579-438e3080-1c43-11ea-9887-18c7b335ef83.PNG)
![14](https://user-images.githubusercontent.com/51121757/70649313-cfed2300-1c44-11ea-8816-19afec1676af.PNG)
![15](https://user-images.githubusercontent.com/51121757/70649501-3114f680-1c45-11ea-8251-6fd40a07de94.PNG)
![16](https://user-images.githubusercontent.com/51121757/70649678-8e10ac80-1c45-11ea-815f-7bdfa5775f93.PNG)
![17](https://user-images.githubusercontent.com/51121757/70649781-bb5d5a80-1c45-11ea-98bd-90b78ac8977a.PNG)

- Note: Possibilty to get some warning after all these steps above. follow the statement given by each warning. 
- For enabling the DNS hostname, go to Action/Edit DNS hostname and click to enable.

```{r}
Create data base 
```
Output of warning
![18](https://user-images.githubusercontent.com/51121757/70650068-48a0af00-1c46-11ea-94ad-31fdd0df41f9.PNG)
![19](https://user-images.githubusercontent.com/51121757/70650073-4c343600-1c46-11ea-8c61-fca3d49d64ab.PNG)

### Step 2: Connect to the database through MySQL workbench

```{r}
MySQL workbench/Setup new connection/
Hostname: it is the endpoint of the database
Username: admin (name put on the Setting Tab) 
Passeword: *****
Test connection then ok
```

![20](https://user-images.githubusercontent.com/51121757/70650726-83efad80-1c47-11ea-8852-0c63d4b96f3c.PNG)
![24](https://user-images.githubusercontent.com/51121757/70651240-5bb47e80-1c48-11ea-849c-dfb58015c769.PNG)
![21](https://user-images.githubusercontent.com/51121757/70650728-85b97100-1c47-11ea-8ef0-647efc905f7f.PNG)
![22](https://user-images.githubusercontent.com/51121757/70650732-87833480-1c47-11ea-94ff-876d66a3493d.PNG)
![23](https://user-images.githubusercontent.com/51121757/70650735-894cf800-1c47-11ea-8965-7f6f40148ec3.PNG)


