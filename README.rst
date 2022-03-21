**This is currently a draft. It might be incorrect, or it might be correct and
give bad advice. Here be dragons.**

==============================
Ren'Py on Steam Deck - A Guide
==============================

The goal of this document is to try to help Ren'Py games pass Steam Deck
compatibility review, and gain "Great on Deck" status, with a minimum amount
of effort from the game's developer.

This isn't a complete guide to getting on Steam itself. There's a very good
document, `Ren’Py Visual Novels on Steam: A Step-by-Step Guide <https://bit.ly/2VOH4vf>`_ by
Bob Conway (bobcgames) that covers this process, that I won't repeat here.

This also isn't a direct substitute for Valve's `Steam Deck documentation <https://partner.steamgames.com/doc/steamdeck>`_,
especially the sections on `How to load and run games on Steam Deck <https://partner.steamgames.com/doc/steamdeck/loadgames>`_ and
the `Steam Deck Compatibility Review Process <https://partner.steamgames.com/doc/steamdeck/compat>`_.

Rather, this is a discussion about how to make sure a Ren'Py game runs on Steam
Deck and satisifies those guidelines. Where possible, I want to try to get the
game running  with minimal changes, though some games will require a re-release.

Linux Build
===========

The Steam Deck is running a build of Linux. Ren'Py is developed on Linux, and
Ren'Py runs well on Linux. It makes a lot of sense to uploade a SteamOS + Linux
build of your game, and make sure that's the build that's submitted for
compatibility testing.

I've seen some problem when running a Windows build through Steam Play and
Proton, and while it may work most of the time, having an unnecessary translation
layer isn't likely to help.


Controller Support
==================

The first requirement is that "Your game must support Steam Deck's physical
controls. The default controller configuration must provide users with the
ability to access all content. Players must not need to adjust any in-game settings
in order to enable controller support or this configuration."

Recommended Controller Mapping
-------------------------------

Since Ren'Py 6.99.6, Ren'Py games include native controller support for the
Xinput-style controller that is emulated by the Steam Input system. The
default mapping of the controls is:

Right Trigger, A
    Dismiss dialogue, select buttons and bars.

Y
    Hide the interface.

Left Shoulder, Left Trigger, Back
    Perform a rollback.

Right Shoulder
    Perform a roll-forward.

Menu/Start
    Enter and exit the game menu.

Left Dpad, Left Stick, Right stick.
    Navigate through the game's interface.

In addition to this, on the Steam Deck, it's suggested that the right touchpad
move the mouse around the screen, and pressing the right touchpad causes a click
to occur.


I'd suggest most games try to map their controllers in this manner, as consitency
will help players adapt to new games.

Ren'Py 6.99.6 and Higher
-------------------------

Since Ren'Py 6.99.6, Ren'Py has had built-in support for controllers, and
that support should work well with Steam Deck, and especially the "Generic Gamepad"
controller configuration. To set this, visit `your dashboard <https://partner.steamgames.com/dashboard>`_,
choose your game:

.. image:: images/deck-1.png

Then navigate to "Edit SteamWorks Settings":

.. image:: images/deck-2.png

And finally, navigate to "Applications", "Steam Input".

.. image:: images/deck-3.png

You can then opt into the "Generic Gamepad" configuration, make sure all kinds
of controllers are opted into Steam Input.

.. image:: images/deck-4.png

When you select "Save", your game should now support generic gamepad input.

**Valve: Do they have to publish after saving?**


Ren'Py 6.99.5 and Lower
-----------------------

**Valve: How do I get the URL for a controller configuration that I created on te deck? Can it be shared between apps?**

Older Ren'Py games don't support the controller input. However, controller
support is very similar to the way Ren'Py navigates games using the keyboard,
and so it's possible to use Steam Input to map the Steam Deck's input to
the keyboard, allowing the game to be accessed.

.. image:: images/deck-1.png

Then navigate to "Edit SteamWorks Settings":

.. image:: images/deck-2.png

And finally, navigate to "Applications", "Steam Input".

.. image:: images/deck-3.png

For the default configuration, choose "Custom Configuraton (Hosted on Steam Workshop)",
then "Add Custom Configuration", and then enter in the URL for the configuration.

When you select "Save", your game should now support mapping the gamepad input to
the keyboard.


Keyboard Support
=================

Another requirement is that "If your game requires text input (eg., for naming a
character or a save file), you must either use a Steamworks API for text entry
to open the on-screen keyboard for players using a controller, or have your
own built-in entry that allows users to enter text in their language using only
a controller."

Many games will trivially satisfy this requirement, by not requiring text
input. Assuming yours doesn't, what you need to do depends on the version
of Ren'Py that you are running.

Ren'Py 7.5.0 or Later
---------------------

(Note that this version is not released at the time of the writing of this
document.)

New versions of Ren'Py include built-in support for managing the Steam Deck
keyboard. Ren'Py will automatically determine if the floating keyboard needs
to be show, and if text input is required, Ren'Py will show the keyboard.
When text input ends, Ren'Py will shift down the keyboard.

There are a few variables that can be set to customize this
process. These live in the _renpysteam namespace, which is the module that
implements them.

\_renpysteam.keyboard\_mode = "always"
    This should be one of "always", "once", and "never".

    * "always" means the keyboard is always show when text input is requested.
    * "once" means the keyboard is shown once per interaction. If the keyboard is hidden, it will not be automatically re-show. (It can be shown again with Steam+X.)
    * "never" means the keyboard should not be automatically managed.

\_renpysteam.keyboard\_shift = True
    If True, interface layers (by default "screens", "transient", and "overlay")
    are shifted upwards so the input text is visible to the user. The input text is shifted
    up so that its baseline is aligned with \_renpysteam.text\_baseline. Input text is
    never shifted down.

\_renpysteam.keyboard\_baseline = 0.5
    This is the baseline that input text is shifted to.

These can be set with the define statement::

    define _renpysteam.keyboard_shift = False


Ren'Py 7.4.11 or Earlier
------------------------

...






This version includes built-in support for managing the Steam Deck keyboard
