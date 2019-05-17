"""
Name:      JK Texty - Store - Code - index.py
Version:   1.0.0
Author:    @Jackkillian
License:   MIT License
========
JK Texty Store
===
This file and others are downloaded by Texty. That is how Texty knows what is in the store.
Each index contains a name and a description.
"""
# Store status (if not good, Texty will give an error and not open the store)
# Statuses: 'True' (up and running) 'False' (error) 'Empty' (empty store)
store_status = 'Empty'

# List of indexes (so Texty will not have to be updated every time a new index is made)
index_list = {'all_index': 'All Add-Ons',
              'popular_index': 'Top Ten Add-Ons',
              'by_jk_index': 'Add-Ons by JK',
              'file_types_index': 'Add-Ons for saving files for other programs',
              'programming_index': 'Add-Ons for programming language IDEs'}

# List of index descriptions
index_list_descriptions = ['All Add-Ons',
                           'Top Ten Add-Ons',
                           'Add-Ons by JK',
                           'Add-Ons for saving files for other programs',
                           'Add-Ons for programming langauge IDEs']

# All index
all_index = {'name': 'description',
             'name': 'description'}

# Top ten popular add-ons
popular_index = {'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description'}

# By JK (Jackkillian) index
by_jk_index = {'name': 'description',
               'name': 'description'}

# File Types index
file_types_index = {'name': 'description',
                    'name': 'description'}

# Programming languges index
programming_index = {'name': 'description',
                     'name': 'description'}
