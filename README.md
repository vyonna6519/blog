# personal-blog
A personal blogging website where one can create and share their opinions and other users can read and comment on them. Additionally,
the application displays random quotes to inspire users. 

## Live Link
[View Site](https://flask-blog-personal.herokuapp.com/)

## Screenshot
Home
![Screenshot from 2022-03-14 20-22-42](https://user-images.githubusercontent.com/93370913/158226691-c408f306-e5f6-430c-a643-7977b9bcd45d.png)

Log In
![Screenshot from 2022-03-14 20-23-11](https://user-images.githubusercontent.com/93370913/158226716-766a02e2-dc6d-4305-9cf9-2f3f42a1f8f5.png)

Sign Up
![Screenshot from 2022-03-14 20-23-15](https://user-images.githubusercontent.com/93370913/158226799-a26f3ca2-9086-4e78-9566-1b28a5702f6d.png)



## User Stories

* View the blog posts on the site
* Comment on blog posts
* View the most recent posts
* See random quotes on the site
* Sign in to the blog
* Create a blog from the application
* Update or delete blogs I have created

## BDD
| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |

| Author login                    | Take you to home page           | Redirect you to the Homepage                 |
| Create a blog post by filling blog form          | Write your blog and post it to blogs    | Your blog is displayed  in index page                     | 
| User comment on the Blog post plus a nickname | Write your feedback and post it | Your feedback is displayed under the blog post   |
| Author delete a blog post       | Deleting the blog post from the database    | The blog post will be deleted and not appear on the page                  |
| update a blog post       | Updating the blog post in database    | The blog post will be updated                |
| delete a comment         | Deleting the blog post in database    | The comment will no longer appear under the post                   |

### Prerequisites

* Python 3.8

## Running the Application
* To run the application, in your terminal:

        $ python3 manage.py server
      
        
## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ cd tests
        $ python3 test_comment.py
        $ python3 test_post.py
        $ python3 test_quote.py
        $ python3 test_user.py
        


## Built With

* [Python](https://www.python.org/) for backend
* [HTML](https://html.com/) for web app structure
* [Bootstrap](https://getbootstrap.com/) and [Javascript](https://www.javascript.com/) for styling
* [Heroku](https://heroku.com)

## Authors

* **Vyonna Njenga** - *Initial work* - [Github](https://github.com/vyonna6519)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


