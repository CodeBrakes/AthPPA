import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
import modules.inputs as inputStream

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True
dcc.Location(id='url', refresh=False),
app.title = 'AthPPA'
app.layout = \
    html.Div(children=[
        html.Div(children=[
            html.P('AthPPA a tool for identifying political popularity using Twitter'),
            # represents the URL bar, doesn't render anything
            dcc.Location(id='url', refresh=False),
            dcc.Link('Graphs Dashboard', href='/index', className="MenuBTN"),
            dcc.Link('How AthPPA works', href='/about_AthPPA', className="MenuBTN"),
            dcc.Link('About us', href='/about_us', className="MenuBTN"),
        ], className="banner"),
        html.P([html.Br()]),
        html.P([html.Br()]),

        html.Div(id='page-content'),

        html.P([html.Br()]),
        html.P([html.Br()]),

        html.Article(children=[
            html.Center([
                html.Img(src='./assets/footer_logo.png', className="footer_logo")
            ])
        ], className="footer")
])



index = html.Div([
    html.P("Graphs Dashboard", className="main_header"),
    html.Br(),

    html.Img(src='./assets/logo_app.png', className="logo"),
    html.P("About this application", className="header"),
    html.P(inputStream.text_1, className="paragraph"),

    html.P("The Hellenic Parliament", className="header"),
    html.P(inputStream.text_2, className="paragraph"),
    html.A("Click to redirect on the official Page of the hellenic parliament",
           href="https://www.hellenicparliament.gr/en/Vouli-ton-Ellinon/O-Thesmos/", target="_blank"),
    html.A("Click to redirect on the Wikipedia Link", href="https://en.wikipedia.org/wiki/Hellenic_Parliament",
           target="_blank"),
    html.P([html.Br()]),
    html.Center([
        html.Img(src='./assets/gr_parliament.png', className="vouli"),
        html.P("The Hellenic parliament and the additional official logo", className="paragraph_image")
    ]),
    html.P("The political landescape in Greece", className="header"),
    html.P(inputStream.text_3, className="paragraph"),
    html.Center([
        html.Img(src='./assets/results.png', className="results"),
        html.P(
            "Results of the last Greek legislative election, showing the vote strength of the party winning a plurality in each electoral district.",
            className="paragraph_image")
    ]),

    html.Div(children=[
        html.Center([
            html.Table([
                html.Tr([
                    html.Td(html.Img(src='./assets/leader1.jpg', className="leader_cards"),
                            className="pol_cell"),
                    html.Td(html.Img(src='./assets/nd.png', className="leader_cards"))
                ])
            ])
        ]),
        html.P(inputStream.text_4, className="paragraph-card")
    ], className="table"),

    dcc.Graph(id='LikesPerTweetLeaderOne',
              figure={
                  'data': [
                      {
                          'y': inputStream.leader_1_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.leader_1_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @kmitsotakis account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f')
                      ),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='textLengthLeaderOne',
              figure={
                  'data': [
                      {
                          'y': inputStream.text_length_leader_1, 'type': 'bar',
                          'name': 'Length of the posted tweet',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      }
                  ],
                  'layout': {
                      'title': 'Text length of the posted tweet mined from @kmitsotakis account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of characters per tweet',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_5, className="paragraph"),

    dcc.Graph(
        id='sentimentLeader_1',
        figure={
            'data': [
                {'values': [inputStream.percentage_pos_ld1, inputStream.percentage_neu_ld1,
                            inputStream.percentage_neg_ld1], 'type': 'pie',
                 'labels': ["Positive Tweets", "Neutral tweets", "Negative Tweets"],
                 'marker': {'colors': ['rgb(46, 112, 97)', 'rgb(112, 122, 128)', 'rgb(194, 81, 81)']}
                 }
            ],
            'layout': dict(
                title='Sentiment analysis of tweets mined from @kmitsotakis account for 200 tweet sample (as percentage)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=13,
                    color='#7f7f7f')
            )
        }
    ),

    dcc.Graph(id='DataForPrAcc',
              figure={
                  'data': [
                      {
                          'y': inputStream.pr_acc_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.pr_acc_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @PrimeministerGR account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_6, className="paragraph"),

    dcc.Graph(
        id='sentimentPrAcc',
        figure={
            'data': [
                {'values': [inputStream.percentage_pos_PrAcc, inputStream.percentage_neu_PrAcc,
                            inputStream.percentage_neg_PrAcc], 'type': 'pie',
                 'labels': ["Positive Tweets", "Neutral tweets", "Negative Tweets"],
                 'marker': {'colors': ['rgb(46, 112, 97)', 'rgb(112, 122, 128)', 'rgb(194, 81, 81)']}
                 }
            ],
            'layout': dict(
                title='Sentiment analysis of tweets mined from @PrimeministerGR account for 200 tweets sample (as percentage)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=13,
                    color='#7f7f7f')
            )
        }
    ),

    dcc.Graph(id='DataForND',
              figure={
                  'data': [
                      {
                          'y': inputStream.tw_pol_party_1_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.tw_pol_party_1_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @neademokratia account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=13,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_7, className="paragraph"),

    dcc.Graph(id='NegHashND_1',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_1,
                          mode='markers',
                          marker=dict(
                              color='#2d5685',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='blue',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#ΝΔ_θελατε) for New Democracy party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )
              }),

    dcc.Graph(id='NegHashND_2',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_2,
                          mode='markers',
                          marker=dict(
                              color='#2d5685',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='blue',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#ΝΔ_ξεφτιλες) for New Democracy party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )

              }),

    dcc.Graph(id='NegHashND_3',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_3,
                          mode='markers',
                          marker=dict(
                              color='#2d5685',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='blue',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#ΝΔ_ρομπες) for New Democracy party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )

              }),

    html.Div(children=[
        html.Center([
            html.Table([
                html.Tr([
                    html.Td(html.Img(src='./assets/leader2.jpg', className="leader_cards"),
                            className="pol_cell"),
                    html.Td(html.Img(src='./assets/syriza.png', className="leader_cards"))
                ])
            ])
        ]),
        html.P(inputStream.text_8, className="paragraph-card")
    ], className="table2"),

    dcc.Graph(id='LikesPerTweetLeaderTwo',
              figure={
                  'data': [
                      {
                          'y': inputStream.leader_2_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'y': inputStream.leader_2_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @atsipras account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='textLengthLeaderTwo',
              figure={
                  'data': [
                      {
                          'y': inputStream.text_length_leader_2, 'type': 'bar',
                          'name': 'Length of the posted tweet',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      }
                  ],
                  'layout': {
                      'title': 'Text length per posted tweet mined from @atsipras account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of characters per tweet',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='DataForSYRIZA',
              figure={
                  'data': [
                      {
                          'y': inputStream.tw_pol_party_2_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'y': inputStream.tw_pol_party_2_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @syriza_gr account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_9, className="paragraph"),

    dcc.Graph(
        id='sentimentLeader_2',
        figure={
            'data': [
                {'values': [inputStream.percentage_pos_ld2, inputStream.percentage_neu_ld2,
                            inputStream.percentage_neg_ld2], 'type': 'pie',
                 'labels': ["Positive Tweets", "Neutral tweets", "Negative Tweets"],
                 'marker': {'colors': ['rgb(46, 112, 97)', 'rgb(112, 122, 128)', 'rgb(194, 81, 81)']}
                 }
            ],
            'layout': dict(
                title='Sentiment analysis of tweets mined from @atsipras account (as percentage)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
        }),

    html.P(inputStream.text_10, className="paragraph"),

    dcc.Graph(id='NegHashSYRIZA_1',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_4,
                          mode='markers',
                          marker=dict(
                              color='#b33250',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='red',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#ΣΥΡΙΖΑ_ξεφτιλες) for SYRIZA party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )
              }),

    dcc.Graph(id='NegHashSYRIZA_2',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_5,
                          mode='markers',
                          marker=dict(
                              color='#b33250',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='red',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#συριζωα) for SYRIZA party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )

              }),

    dcc.Graph(id='NegHashSYRIZA_3',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_6,
                          mode='markers',
                          marker=dict(
                              color='#b33250',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='red',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#Συριζα_απατεωνες) for SYRIZA party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )

              }),

    html.Div(children=[
        html.Center([
            html.Table([
                html.Tr([
                    html.Td(html.Img(src='./assets/leader3.jpg', className="leader_cards"),
                            className="pol_cell"),
                    html.Td(html.Img(src='./assets/pasok.png', className="leader_cards"))
                ])
            ])
        ]),
        html.P(inputStream.text_11, className="paragraph-card")
    ], className="table3"),

    dcc.Graph(id='LikesPerTweetLeaderThree',
              figure={
                  'data': [
                      {
                          'y': inputStream.leader_3_likes, 'type': 'bar', 'name': 'Tweet Likes',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      },
                      {
                          'y': inputStream.leader_3_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'User likes and re-tweets per posted tweet mined from @FofiGennimata account (200 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='textLengthLeaderThree',
              figure={
                  'data': [
                      {
                          'y': inputStream.text_length_leader_3, 'type': 'bar',
                          'name': 'Length of the posted tweet',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Text length per posted tweet mined from @FofiGennimata account (200 tweets sample',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of characters per tweet',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_12, className="paragraph"),

    dcc.Graph(
        id='sentimentLeader_3',
        figure={
            'data': [
                {'values': [inputStream.percentage_pos_ld3, inputStream.percentage_neu_ld3,
                            inputStream.percentage_neg_ld3], 'type': 'pie',
                 'labels': ["Positive Tweets", "Neutral tweets", "Negative Tweets"],
                 'marker': {'colors': ['rgb(46, 112, 97)', 'rgb(112, 122, 128)', 'rgb(194, 81, 81)']}
                 }
            ],
            'layout': dict(
                title='Sentiment analysis of tweets mined from @fofigennimata account (as percentage)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
        }
    ),

    dcc.Graph(id='DataForLeaderThree',
              figure={
                  'data': [
                      {
                          'y': inputStream.tw_pol_party_3_likes, 'type': 'bar', 'name': 'Tweet likes',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      },
                      {
                          'y': inputStream.tw_pol_party_3_retweets, 'type': 'line', 'name': 'Retweets'
                      }
                  ],
                  'layout': {
                      'title': 'Data mined from tweets made by the official Movement for Change Twitter account (@kinimallagis)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    html.P(inputStream.text_13, className="paragraph"),

    dcc.Graph(id='NegHashKINAL_1',
              figure={
                  'data': [
                      go.Scatter(
                          x=inputStream.neg_res_7,
                          mode='markers',
                          marker=dict(
                              color='#2f8f64',
                              opacity=0.5,
                              size=18,
                              line=dict(
                                  color='green',
                                  width=1
                              )
                          )
                      )

                  ],
                  'layout': go.Layout(
                      title='Mined tweets based on negative hashtag (#ΚΙΝΑΛ_ξεφτιλες) for KINAL party (200 tweets sample)',
                      xaxis={'title': 'Date tweet posted'},
                      yaxis={'title': 'Obtained tweets'},
                  )
              }),

    html.Div([
        html.Center([
            html.Img(src='./assets/conclusion.png', className="conclusion")])
    ], className="table4"),
    dcc.Graph(id='LikesPerTweetAll',
              figure={
                  'data': [
                      {
                          'y': inputStream.leader_1_likes, 'type': 'line',
                          'name': 'Kyriakos Mitsotakis - New Democracy',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.leader_2_likes, 'type': 'line', 'name': 'Alexis Tsipras - SYRIZA',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'y': inputStream.leader_3_likes, 'type': 'line', 'name': 'Fofi Gennimata - KINAL',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Number of likes per tweet for top three Greek political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of likes and retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),
    dcc.Graph(id='re-share_per_tweet',
              figure={
                  'data': [
                      {
                          'y': inputStream.leader_1_retweets, 'type': 'line',
                          'name': 'Kyriakos Mitsotakis - New Democracy',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.leader_2_retweets, 'type': 'line', 'name': 'Alexis Tsipras - SYRIZA',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'y': inputStream.leader_3_retweets, 'type': 'line', 'name': 'Fofi Genimata - KINAL',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Number of re-tweets per tweet for top three Greek political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Number of tweet samples',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of retweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='total_subscribers',
              figure={
                  'data': [
                      {
                          'x': [1], 'y': [inputStream.follower_count_leader_1], 'type': 'bar',
                          'name': 'Kyriakos Mitsotakis - New Democracy',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'x': [2], 'y': [inputStream.follower_count_leader_2], 'type': 'bar',
                          'name': 'Alexis Tsipras - SYRIZA',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'x': [3], 'y': [inputStream.follower_count_leader_3], 'type': 'bar',
                          'name': 'Fofi Grennimata - KINAL',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Registered subscribers per Twitter account (actual numbers)',
                      'xaxis': dict(
                          title='Number of political leaders',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of followers',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(
        id='totalSubscribers',
        figure={
            'data': [
                {'values': [inputStream.percentage_leader_1, inputStream.percentage_leader_2,
                            inputStream.percentage_leader_3], 'type': 'pie',
                 'labels': ["Kyriakos Mitsotakis - New Democracy", "Alexis Tsipras - SYRIZA",
                            "Fofi Gennimata - KINAL"],
                 'marker': {'colors': ['rgb(45, 86, 133)', 'rgb(179, 50, 80)', 'rgb(47, 143, 100)']}
                 }
            ],
            'layout': dict(
                title='Registered subscribers per Twitter account (as percentage)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
        }),

    dcc.Graph(id='totalsentimentComparison',
              figure={
                  'data': [
                      {
                          'y': inputStream.sentiment_leader_1, 'type': 'line',
                          'name': 'Kyriakos Mitsotakis - New Democracy',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'y': inputStream.sentiment_leader_2, 'type': 'line', 'name': 'Alexis Tsipras - SYRIZA',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'y': inputStream.sentiment_leader_3, 'type': 'line', 'name': 'Fofi Genimata - KINAL',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Total comparison of sentiment analysis for the top three Greek political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Numbers of a single tweet sample',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Sentiment value indicator',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(id='totalPOSsentimentComparison',
              figure={
                  'data': [
                      {
                          'x': [1], 'y': [inputStream.pos_count_leader1], 'type': 'bar',
                          'name': 'Kyriakos Mitsotakis - New Democracy (200 tweet sample)',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'x': [2], 'y': [inputStream.pos_count_leader2], 'type': 'bar',
                          'name': 'Alexis Tsipras - SYRIZA (200 tweet sample)',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'x': [3], 'y': [inputStream.pos_count_leader3], 'type': 'bar',
                          'name': 'Fofi Grennimata - KINAL (200 tweet sample)',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Positive identified tweets for the top three political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Number of political leaders',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of positive tweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),

    dcc.Graph(
        id='totalPOSsentimentComparisonPercentage',
        figure={
            'data': [
                {'values': [inputStream.percentage_pos_ld1, inputStream.percentage_pos_ld2,
                            inputStream.percentage_pos_ld3], 'type': 'pie',
                 'labels': ["Kyriakos Mitsotakis - New Democracy (200 tweet sample)", "Alexis Tsipras - SYRIZA (200 tweet sample)",
                            "Fofi Gennimata - KINAL (200 tweet sample)"],
                 'marker': {'colors': ['rgb(45, 86, 133)', 'rgb(179, 50, 80)', 'rgb(47, 143, 100)']}
                 }
            ],
            'layout': dict(
                title='Positive identified tweets for the top three political leaders (600 tweets sample) as percentage',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
    }),

    dcc.Graph(id='totalNEUsentimentComparison',
              figure={
                  'data': [
                      {
                          'x': [1], 'y': [inputStream.neu_count_leader1], 'type': 'bar',
                          'name': 'Kyriakos Mitsotakis - New Democracy (200 tweet sample)',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'x': [2], 'y': [inputStream.neu_count_leader2], 'type': 'bar',
                          'name': 'Alexis Tsipras - SYRIZA (200 tweet sample)',
                          'marker': {'color': 'rgb(179, 50, 80) (200 tweet sample)'}
                      },
                      {
                          'x': [3], 'y': [inputStream.neu_count_leader3], 'type': 'bar',
                          'name': 'Fofi Grennimata - KINAL (200 tweet sample)',
                          'marker': {'color': 'rgb(47, 143, 100) (200 tweet sample)'}
                      }
                  ],
                  'layout': {
                      'title': 'Neutral identified tweets for the top three political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Number of political leaders',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of neutral tweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
    }),

    dcc.Graph(
        id='totalNEUsentimentComparisonPercentage',
        figure={
            'data': [
                {'values': [inputStream.percentage_neu_ld1, inputStream.percentage_neu_ld2,
                            inputStream.percentage_neu_ld3], 'type': 'pie',
                 'labels': ["Kyriakos Mitsotakis - New Democracy (200 tweet sample)", "Alexis Tsipras - SYRIZA (200 tweet sample)",
                            "Fofi Gennimata - KINAL (200 tweet sample)"],
                 'marker': {'colors': ['rgb(45, 86, 133)', 'rgb(179, 50, 80)', 'rgb(47, 143, 100)']}
                 }
            ],
            'layout': dict(
                title='Neutral identified tweets for the top three political leaders (600 tweets sample) as percentage',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
    }),

    dcc.Graph(id='totalNEGsentimentComparison',
              figure={
                  'data': [
                      {
                          'x': [1], 'y': [inputStream.neg_count_leader1], 'type': 'bar',
                          'name': 'Kyriakos Mitsotakis - New Democracy (200 tweet sample)',
                          'marker': {'color': 'rgb(45, 86, 133)'}
                      },
                      {
                          'x': [2], 'y': [inputStream.neg_count_leader2], 'type': 'bar',
                          'name': 'Alexis Tsipras - SYRIZA (200 tweet sample)',
                          'marker': {'color': 'rgb(179, 50, 80)'}
                      },
                      {
                          'x': [3], 'y': [inputStream.neg_count_leader3], 'type': 'bar',
                          'name': 'Fofi Grennimata - KINAL (200 tweet sample)',
                          'marker': {'color': 'rgb(47, 143, 100)'}
                      }
                  ],
                  'layout': {
                      'title': 'Negative identified tweets for the top three political leaders (600 tweets sample)',
                      'xaxis': dict(
                          title='Number of political leaders',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f')),
                      'yaxis': dict(
                          title='Number of negative tweets',
                          titlefont=dict(
                              family='Courier New, monospace',
                              size=14,
                              color='#7f7f7f'))
                  }
              }),
    dcc.Graph(
        id='totalNEGsentimentComparisonPercentage',
        figure={
            'data': [
                {'values': [inputStream.percentage_neg_ld1, inputStream.percentage_neg_ld2,
                            inputStream.percentage_neg_ld3], 'type': 'pie',
                 'labels': ["Kyriakos Mitsotakis - New Democracy (200 tweet sample)", "Alexis Tsipras - SYRIZA (200 tweet sample)",
                            "Fofi Gennimata - KINAL (200 tweet sample)"],
                 'marker': {'colors': ['rgb(45, 86, 133)', 'rgb(179, 50, 80)', 'rgb(47, 143, 100)']}
                 }
            ],
            'layout': dict(
                title='Negative identified tweets for the top three political leaders (600 tweets sample) as percentage',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=14,
                    color='#7f7f7f')
            )
    })
])

about_AthPPA = html.Div([
    html.P("How AthPPA works", className="main_header"),
    html.Br(),

    html.P("Why to choose Twitter as data source", className="header"),
    html.P(inputStream.aboutapp_text_1, className="paragraph"),

    html.P("How AthPPA communicates with Twitter", className="header"),
    html.P(inputStream.aboutapp_text_2, className="paragraph"),

    html.Center([
        html.Img(src='./assets/twitter_example.png', className="tw_example_image"),
        html.P(
            "Figure 1: Overall structure of tweet retrieval using a Twitter API as well as its authentication",
            className="paragraph_image")
    ]),

    html.Br(),
    html.P(inputStream.aboutapp_text_3, className="paragraph"),

    html.Br(),

    html.P("How AthPPA sentiment analyzer works", className="header"),
    html.P(inputStream.aboutapp_text_4, className="paragraph"),

    html.A("Click here for Greek Spacy module made by Giannis Daras",
           href="https://github.com/eellak/gsoc2018-spacy", target="_blank"),
    html.Br(),
    html.Br(),
    html.A("Click here Greek sentiment lexicon of Adam Tsakalidis",
           href="https://github.com/MKLab-ITI/greek-sentiment-lexicon", target="_blank"),

    html.Br(),
    html.Center([
        html.Table([
            html.Tr([
                html.Th("Sentiment Value", className="cel1_tbsent"),
                html.Th("Emotion score Type", className="cel2_tbsent")
            ]),
            html.Tr([
                html.Td("3", className="cel1_tbsent"),
                html.Td("Hapiness", className="cel2_tbsent")
            ], className="colored_row_sent"),
            html.Tr([
                html.Td("2", className="cel1_tbsent"),
                html.Td("Surprise", className="cel2_tbsent")
            ], className="white_row_sent"),
            html.Tr([
                html.Td("1", className="cel1_tbsent"),
                html.Td("Sadness", className="cel2_tbsent")
            ], className="colored_row_sent"),
            html.Tr([
                html.Td("0", className="cel1_tbsent"),
                html.Td("Neutral", className="cel2_tbsent")
            ], className="white_row_sent"),
            html.Tr([
                html.Td("-1", className="cel1_tbsent"),
                html.Td("Fear", className="cel2_tbsent")
            ], className="colored_row_sent"),
            html.Tr([
                html.Td("-2", className="cel1_tbsent"),
                html.Td("Disgust", className="cel2_tbsent")
            ], className="white_row_sent"),
            html.Tr([
                html.Td("-3", className="cel1_tbsent"),
                html.Td("Anger", className="cel2_tbsent")
            ], className="colored_row_sent")
        ], className="sentiment-table")
    ]),

    html.P("Table 1: Sentiment values used for the labelling process by AthPPA", className="paragraph_image"),
    html.Div(id='about_AthPPA-content')
])


about_us = html.Div([
    html.P("About us", className="main_header"),
    html.Br(),

    html.Table([
        html.Tr([
            html.Th([
                html.P("Alexandros Britzolakis MSc in Informatics Engineering, H.M.U", className="header-about"),
                html.P("Former graduate assistant researcher, CBML-FORTH-ICS and at AISE-H.M.U.", className="header-about")
            ], className="row-about"),

            html.Th([
                html.P("Nikos Papadakis PhD in Computer Science, UoC", className="header-about"),
                html.P("Associate proffessor at E.C.E. department, H.M.U.", className="header-about")
            ])
        ], className="row-about"),
        html.Tr([
                html.Td([html.P(inputStream.about_text_1, className="paragraph")]),
                html.Td([html.P(inputStream.about_text_2, className="paragraph")])
        ]),

        html.Tr([
            html.Th([
                html.P("Haridimos Kondylakis, PhD in Computer Science UoC", className="header-about"),
                html.P("Adjunct lecturer at E.C.E. department, H.M.U.", className="header-about")
            ], className="row-about"),

            html.Th([
                html.P("Stelios Sfakianakis, PhD in Biotechnology, TUC", className="header-about"),
                html.P("Adjunct lecturer at E.C.E. department, H.M.U.", className="header-about")
            ], className="row-about")
        ]),
        html.Tr([
            html.Td([html.P(inputStream.about_text_3, className="paragraph")]),
            html.Td([html.P(inputStream.about_text_4, className="paragraph")])
        ]),

    ], className="table-about")
])


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about_AthPPA':
        return about_AthPPA
    elif pathname == '/about_us':
        return about_us
    else:
        return index
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=False)
