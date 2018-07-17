from flask import Flask, render_template,redirect
import numpy as np
import pandas as pd
from train import train
from forms import forms


app = Flask(__name__)
app.config.from_object('config')

items = pd.read_csv('ml-latest-small/movies.csv', sep = ',', encoding = 'latin-1')

movie = items['title']


@app.route('/', methods = ['GET','POST'])
def index():
    form = forms.HomeForm()

    global movieList2
    movieList2 = train.movies()

    global movieList 
    movieList = []
    for i in movieList2:
        name = movie[i]
        movieList.append(name)

    global ratingsList
    ratingsList = []

    if form.validate_on_submit():
        return redirect ('/movie1')
    return render_template('index.html', form = form)

@app.route('/movie1', methods = ['GET', 'POST'])
def movie1():
    form1 = forms.RatingForm()
    movieName = movieList[0]
    if form1.validate_on_submit():
        ratingsList.append(form1.rating.data)
        return redirect ('/movie2')
    return render_template('ratings.html', movieName = movieName, form=form1)

@app.route('/movie2', methods = ['GET', 'POST'])
def movie2():
    form2 = forms.RatingForm()
    movieName = movieList[1]
    if form2.validate_on_submit():
        ratingsList.append(form2.rating.data)
        return redirect('/movie3')
    return render_template('ratings.html', movieName = movieName, form=form2)

@app.route('/movie3', methods = ['GET', 'POST'])
def movie3():
    form3 = forms.RatingForm()
    movieName = movieList[2]
    if form3.validate_on_submit():
        ratingsList.append(form3.rating.data)
        return redirect('/movie4')
    return render_template('ratings.html', movieName = movieName, form=form3)

@app.route('/movie4', methods = ['GET', 'POST'])
def movie4():
    form4 = forms.RatingForm()
    movieName = movieList[3]
    if form4.validate_on_submit():
        ratingsList.append(form4.rating.data)
        return redirect('/movie5')
    return render_template('ratings.html', movieName = movieName, form=form4)

@app.route('/movie5', methods = ['GET', 'POST'])
def movie5():
    form5 = forms.RatingForm()
    movieName = movieList[4]
    if form5.validate_on_submit():
        ratingsList.append(form5.rating.data)
        return redirect('/movie6')
    return render_template('ratings.html', movieName = movieName, form=form5)

@app.route('/movie6', methods = ['GET', 'POST'])
def movie6():
    form6 = forms.RatingForm()
    movieName = movieList[5]
    if form6.validate_on_submit():
        ratingsList.append(form6.rating.data)
        return redirect('/movie7')
    return render_template('ratings.html', movieName = movieName, form=form6)


@app.route('/movie7', methods = ['GET', 'POST'])
def movie7():
    form7 = forms.RatingForm()
    movieName = movieList[6]
    if form7.validate_on_submit():
        ratingsList.append(form7.rating.data)
        return redirect('/movie8')
    return render_template('ratings.html', movieName = movieName, form=form7)


@app.route('/movie8', methods = ['GET', 'POST'])
def movie8():
    form8 = forms.RatingForm()
    movieName = movieList[7]
    if form8.validate_on_submit():
        ratingsList.append(form8.rating.data)
        return redirect('/movie9')
    return render_template('ratings.html', movieName = movieName, form=form8)

@app.route('/movie9', methods = ['GET', 'POST'])
def movie9():
    form9 = forms.RatingForm()
    movieName = movieList[8]
    if form9.validate_on_submit():
        ratingsList.append(form9.rating.data)
        return redirect('/movie10')
    return render_template('ratings.html', movieName = movieName, form=form9)


@app.route('/movie10', methods = ['GET', 'POST'])
def movie10():
    form10 = forms.RatingForm()
    movieName = movieList[9]
    if form10.validate_on_submit():
        ratingsList.append(form10.rating.data)
        return redirect('/movie11')
    return render_template('ratings.html', movieName = movieName, form=form10)

@app.route('/movie11', methods = ['GET', 'POST'])
def movie11():
    form11 = forms.RatingForm()
    movieName = movieList[10]
    if form11.validate_on_submit():
        ratingsList.append(form11.rating.data)
        return redirect('/movie12')
    return render_template('ratings.html', movieName = movieName, form=form11)


@app.route('/movie12', methods = ['GET', 'POST'])
def movie12():
    form12 = forms.RatingForm()
    movieName = movieList[11]
    if form12.validate_on_submit():
        ratingsList.append(form12.rating.data)
        return redirect('/movie13')
    return render_template('ratings.html', movieName = movieName, form=form12)


@app.route('/movie13', methods = ['GET', 'POST'])
def movie13():
    form13 = forms.RatingForm()
    movieName = movieList[12]
    if form13.validate_on_submit():
        ratingsList.append(form13.rating.data)
        return redirect('/movie14')
    return render_template('ratings.html', movieName = movieName, form=form13)


@app.route('/movie14', methods = ['GET', 'POST'])
def movie14():
    form14 = forms.RatingForm()
    movieName = movieList[13]
    if form14.validate_on_submit():
        ratingsList.append(form14.rating.data)
        return redirect('/movie15')
    return render_template('ratings.html', movieName = movieName, form=form14)


@app.route('/movie15', methods = ['GET', 'POST'])
def movie15():
    form15 = forms.RatingForm()
    movieName = movieList[14]
    if form15.validate_on_submit():
        ratingsList.append(form15.rating.data)
        return redirect('/movie16')
    return render_template('ratings.html', movieName = movieName, form=form15)

@app.route('/movie16', methods = ['GET', 'POST'])
def movie16():
    form16 = forms.RatingForm()
    movieName = movieList[15]
    if form16.validate_on_submit():
        ratingsList.append(form16.rating.data)
        return redirect('/movie17')
    return render_template('ratings.html', movieName = movieName, form=form16)

@app.route('/movie17', methods = ['GET', 'POST'])
def movie17():
    form17 = forms.RatingForm()
    movieName = movieList[16]
    if form17.validate_on_submit():
        ratingsList.append(form17.rating.data)
        return redirect('/movie18')
    return render_template('ratings.html', movieName = movieName, form=form17)

@app.route('/movie18', methods = ['GET', 'POST'])
def movie18():
    form18 = forms.RatingForm()
    movieName = movieList[17]
    if form18.validate_on_submit():
        ratingsList.append(form18.rating.data)
        return redirect('/movie19')
    return render_template('ratings.html', movieName = movieName, form=form18)

@app.route('/movie19', methods = ['GET', 'POST'])
def movie19():
    form19 = forms.RatingForm()
    movieName = movieList[18]
    if form19.validate_on_submit():
        ratingsList.append(form19.rating.data)
        return redirect('/movie20')
    return render_template('ratings.html', movieName = movieName, form=form19)

@app.route('/movie20', methods = ['GET', 'POST'])
def movie20():
    form20 = forms.RatingForm()
    movieName = movieList[19]
    if form20.validate_on_submit():
        ratingsList.append(form20.rating.data)
        return redirect('/recommend')
    return render_template('ratings.html', movieName = movieName, form=form20)


@app.route('/recommend', methods = ['GET', 'POST'])
def recommend():
    form21 = forms.RestartForm()
    recList = train.recommend(movieList2, ratingsList)
    movie1 = recList[0]
    movie2 = recList[1]
    movie3 = recList[2]
    movie4 = recList[3]
    movie5 = recList[4]
    if form21.validate_on_submit():
        return redirect('/')
    return render_template('recommend.html', movie1 = movie1, movie2 = movie2, movie3 = movie3, movie4 = movie4, movie5 = movie5, form =form21)

if __name__ == '__main__':
    app.run(debug =True)

