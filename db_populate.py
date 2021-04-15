from main.run import db, Winery, Winemaker, Wine

# Populating Winemakers
# ------------------------------------------------------------------------------------------------------------------

winemaker_data=[{
    "id": 1,
    "name": "José Lovaglio",
    "genres": ["malbec","chardonnay","merlot"],
    "city": "Lujan de Cuyo",
    "state": "Mendoza",
    "phone": "234592735",
    "website": "http://www.joselovaglio.com",
    "facebook_link": "http://www.facebook.com/jlovaglio",
    "seeking_winery": True,
    "seeking_description": "Hi I'm a winemaker from Agrelo seeking for a winery to make my wines",
    "image_link": "https://images.unsplash.com/flagged/photo-1595514191830-3e96a518989b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
    "past_wines": [{
      "winery_id": 1,
      "winery_name": "Susana Balbo Wines",
      "winery_image_link": "https://images.unsplash.com/photo-1572913017567-02f0649bc4fd?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_wines": [],
    "past_wines_count": 1,
    "upcoming_wines_count": 0,
  }, {
    "id": 2,
    "name": "Gustavo Bertagna",
    "genres": ["torrontes", "malbec", "chenin"],
    "city": "Agrelo",
    "state": "Mendoza",
    "phone": "3004005000",
    "facebook_link": "http://www.facebook.com/gbertagna",
    "seeking_winery": False,
    "image_link": "https://images.unsplash.com/flagged/photo-1595514191830-3e96a518989b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
    "past_wines": [{
      "winery_id": 3,
      "winery_name": "Vaglio Wines",
      "winery_image_link": "https://images.unsplash.com/photo-1573061750909-d2586d3fe8b8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "upcoming_wines": [],
    "past_wines_count": 1,
    "upcoming_wines_count": 0,
  }, {
    "id": 3,
    "name": "David Bonomi",
    "genres": ["malbec", "cabernet franc"],
    "city": "Tupungato",
    "state": "Mendoza",
    "phone": "4323255432",
    "facebook_link": "http://www.facebook.com/dbonomi",
    "seeking_winery": False,
    "image_link": "https://images.unsplash.com/photo-1598226863630-2826f1d31532?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1534&q=80",
    "past_wines": [],
    "upcoming_wines": [{
      "winery_id": 3,
      "winery_name": "Vaglio Wines",
      "winery_image_link": "https://images.unsplash.com/photo-1573061750909-d2586d3fe8b8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }, {
      "winery_id": 3,
      "winery_name": "Vaglio Wines",
      "winery_image_link": "https://images.unsplash.com/photo-1573061750909-d2586d3fe8b8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }, {
      "winery_id": 3,
      "winery_name": "Vaglio Wines",
      "winery_image_link": "https://images.unsplash.com/photo-1573061750909-d2586d3fe8b8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "past_wines_count": 0,
    "upcoming_wines_count": 3,
  }]

def populate_winemakers():
    for winemaker in winemaker_data:
        data = Winemaker(
            id = winemaker["id"],
            name = winemaker["name"],
            genres = winemaker["genres"],
            city = winemaker["city"],
            state = winemaker["state"],
            phone = winemaker["phone"],
            # website = winemaker["website"],
            facebook_link = winemaker["facebook_link"],
            seeking_winery = winemaker["seeking_winery"],
            # seeking_description = winemaker["seeking_description"],
            image_link = winemaker["image_link"],
            # past_wines = winemaker["past_wines"],
            # upcoming_wines = winemaker["upcoming_wines"],
            # past_wines_count = winemaker["past_wines_count"],
            # upcoming_wines_count = winemaker["upcoming_wines_count"]
        )
        db.session.add(data)

    # id4 = Winemaker.query.get(4)
    # id4.facebook_link = winemaker_data[0]["facebook_link"]
    # id4.website = winemaker_data[0]["website"]
    # id4.seeking_description = winemaker_data[0]["seeking_description"]
    # db.session.add(id4)

    # id5 = Winemaker.query.get(5)
    # id5.facebook_link = winemaker_data[0]["facebook_link"]
    # db.session.add(id5)

    db.session.commit()


# Populating Wineries
# ------------------------------------------------------------------

wineries_data=[{
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"], # missing in winery
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com", # missing in winery
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True, # missing in winery
    "seeking_description": "We are on the lookout for a local winemaker to play every two weeks. Please call us.", # missing in winery
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    "past_wines": [{
      "winemaker_id": 4,
      "winemaker_name": "Guns N Petals",
      "winemaker_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }], # missing in winery
    "upcoming_wines": [], # missing in winery
    "past_wines_count": 1, # missing in winery
    "upcoming_wines_count": 0, # missing in winery
  },{
    "id": 2,
    "name": "The Dueling Pianos Bar",
    "genres": ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "website": "https://www.theduelingpianos.com",
    "facebook_link": "https://www.facebook.com/theduelingpianos",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
    "past_wines": [],
    "upcoming_wines": [],
    "past_wines_count": 0,
    "upcoming_wines_count": 0,
  },{
    "id": 3,
    "name": "Park Square Live Music & Coffee",
    "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "website": "https://www.parksquarelivemusicandcoffee.com",
    "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "past_wines": [{
      "winemaker_id": 5,
      "winemaker_name": "Matt Quevedo",
      "winemaker_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "upcoming_wines": [{
      "winemaker_id": 6,
      "winemaker_name": "The Wild Sax Band",
      "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-01T20:00:00.000Z"
    }, {
      "winemaker_id": 6,
      "winemaker_name": "The Wild Sax Band",
      "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-08T20:00:00.000Z"
    }, {
      "winemaker_id": 6,
      "winemaker_name": "The Wild Sax Band",
      "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-15T20:00:00.000Z"
    }],
    "past_wines_count": 1,
    "upcoming_wines_count": 1,
  }]

def populate_wineries():
    for winery in wineries_data:
        data = Winery(
            id = winery["id"],
            name = winery["name"],
            genres = winery["genres"],
            address = winery["address"],
            city = winery["city"],
            state = winery["state"],
            phone = winery["phone"],
            website = winery["website"],
            facebook_link = winery["facebook_link"],
            seeking_talent = winery["seeking_talent"],
            # seeking_description = winery["seeking_description"],
            image_link = winery["image_link"],
            # past_wines = winery["past_wines"],
            # upcoming_wines = winery["upcoming_wines"],
            # past_wines_count = winery["past_wines_count"],
            # upcoming_wines_count = winery["upcoming_wines_count"]
        )
        db.session.add(data)

    id1 = Winery.query.get(1)
    id1.seeking_description = winemaker_data[0]["seeking_description"]
    db.session.add(id1)

    db.session.commit()


# Populating Wines
# ----------------------------------------------------------------------------

wines_data=[{
    "winery_id": 1,
    "winery_name": "The Musical Hop",
    "winemaker_id": 4,
    "winemaker_name": "Guns N Petals",
    "winemaker_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
    }, {
    "winery_id": 3,
    "winery_name": "Park Square Live Music & Coffee",
    "winemaker_id": 5,
    "winemaker_name": "Matt Quevedo",
    "winemaker_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
    }, {
    "winery_id": 3,
    "winery_name": "Park Square Live Music & Coffee",
    "winemaker_id": 6,
    "winemaker_name": "The Wild Sax Band",
    "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
    }, {
    "winery_id": 3,
    "winery_name": "Park Square Live Music & Coffee",
    "winemaker_id": 6,
    "winemaker_name": "The Wild Sax Band",
    "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
    }, {
    "winery_id": 3,
    "winery_name": "Park Square Live Music & Coffee",
    "winemaker_id": 6,
    "winemaker_name": "The Wild Sax Band",
    "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
    }]

def populate_wines():
    for wine in wines_data:
        data = Wine(
            winery_id = wine["winery_id"],
            winemaker_id = wine["winemaker_id"],
            start_time = wine["start_time"],
            # address = wine["address"],
            # city = wine["city"],
            # state = wine["state"],
            # phone = wine["phone"],
            # website = wine["website"],
            # facebook_link = wine["facebook_link"],
            # seeking_talent = wine["seeking_talent"],
            # # seeking_description = wine["seeking_description"],
            # image_link = wine["image_link"],
            # past_wines = wine["past_wines"],
            # upcoming_wines = wine["upcoming_wines"],
            # past_wines_count = wine["past_wines_count"],
            # upcoming_wines_count = wine["upcoming_wines_count"]
        )
        db.session.add(data)

    db.session.commit()



def populate_winery_2_after_delete_test_postman():
    data = Winery(
            id = wineries_data[1]["id"],
            name = wineries_data[1]["name"],
            genres = wineries_data[1]["genres"],
            address = wineries_data[1]["address"],
            city = wineries_data[1]["city"],
            state = wineries_data[1]["state"],
            phone = wineries_data[1]["phone"],
            website = wineries_data[1]["website"],
            facebook_link = wineries_data[1]["facebook_link"],
            seeking_talent = wineries_data[1]["seeking_talent"],
            # seeking_description = wineries_data[1]["seeking_description"],
            image_link = wineries_data[1]["image_link"],
            # past_wines = wineries_data[1]["past_wines"],
            # upcoming_wines = wineries_data[1]["upcoming_wines"],
            # past_wines_count = wineries_data[1]["past_wines_count"],
            # upcoming_wines_count = wineries_data[1]["upcoming_wines_count"]
        )
    db.session.add(data)
    db.session.commit()
    print(f'added {wineries_data[1]["name"]} back to the database')





# function execution
# ----------------------------------------------------------------------------

populate_winemakers() # uncheck to populate
# populate_wineries() # uncheck to populate
# populate_wines() # uncheck to populate.

# populate_winery_2_after_delete_test_postman() # uncheck to add winery id=1 back to the database after postman DELETE endpoint testing