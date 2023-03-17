.. _horizonsInterfaces:

New Horizons Requirements
=========================

We continue our case here about the imaginary company New Horizons as introduced
in the previous section :ref:`newHorizons` . We focus here on the exact
requirements for processing an accepted booking, in particular the
way it should be stored in a relational database. The relational
database is for internal use by New Horizons and can be developed
from scratch.

.. highlight:: none

The database we want to fill has the following tables: ::

  Table booking
  -------------

  id: int, primary key
  travelerId: int
  price: money
  fee: booking

  Table visit
  -----------

  bookingId: int, part of primary key, foreign key referencing booking
  seq: int, part of primary key
  hostId: int
  productId: int
  startDate: date
  endDate: date
  price: money

Note that bookings, hosts and travelers are referenced by integer id fields.
Additional information about travelers and hosts, like name, address,
telephone are omitted because they do not have to be stored with a
booking. Every visit has a price, the amount that should be paid
to the host. In table booking, we store the price that should be
paid by the traveler to New Horizons, and the fee kept by New
Horizons. Each visit has a productId that references
some other table that is not elaborated here. That other table
links a product id to a room number in a hotel, a particular
spot on a camping, or some other description of the accommodation
ordered. Finally, each visit has a start date and an end date.

We assume that the acceptance of a booking is preceded by some
user interaction in which the user selects destinations and picks
dates. Therefore, the values of the booking id, the traveler id,
the host id and the product id can appear in the incoming message for
accepted bookings. We finish this section with an example of an
accepted booking:

.. literalinclude:: validBooking.xml
   :language: xml

