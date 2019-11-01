#!/usr/bin/env python
# -*- coding: utf-8 -*-
import client

def Messages(user):

    if client.getUserLanguage(user)=="RU":
    
        MESSAGES = {
            'start': client.getMessage(1),
            
            'language': client.getMessage(2),

            'area': client.getMessage(3),
            'flat': client.getMessage(4),
            'land': client.getMessage(5),
            'free_area': client.getMessage(6),

            'title_added': client.getMessage(7),

            'region_added': client.getMessage(8),

            'geo1': client.getMessage(9),
            'geo2': client.getMessage(10),
            'geo3': client.getMessage(11),

            'area_started': client.getMessage(12),
            'flat_started': client.getMessage(13),
            'land_started': client.getMessage(14),
            'free_area_started': client.getMessage(15),

            'area_rooms_added': client.getMessage(16),
            'area_square_added': client.getMessage(17),
            
            'flat_rooms_added': client.getMessage(16),
            'flat_square_added': client.getMessage(17),

            'land_square_added': client.getMessage(17),

            'free_area_square_added': client.getMessage(17),
            'free_area_state_added': client.getMessage(14),

            'photo1': client.getMessage(18),
            'photo2': client.getMessage(19),
            'photo3': client.getMessage(20),

            'ammount': client.getMessage(21),
            'ammount_set': client.getMessage(22),

            'contacts': client.getMessage(23),

            'price_list': client.getMessage(24),

            'choose_action': client.getMessage(25),
            'filter': client.getMessage(26),
            'send_text': client.getMessage(27),

            'choose_photo_edit': client.getMessage(28),

            'edit_text_now': client.getMessage(29),

            'data_clear': client.getMessage(30),

            "digits_only": client.getMessage(31),

            "price_list2": client.getMessage(32),

            "filters_clear": client.getMessage(65),
            "prop_state": client.getMessage(66),
            "no_ann": client.getMessage(67),
            "main_floor": client.getMessage(71),
            "floor": client.getMessage(72),

            'area_search': client.getMessage(75),
            'flat_search': client.getMessage(76),
            'land_search': client.getMessage(77),
            'free_area_search': client.getMessage(78),

            'choose_action_after_language': client.getMessage(83),
            'choose_action_rent': client.getMessage(84),
            'choose_action_sale': client.getMessage(85),
            'choose_action_search': client.getMessage(86),

            'moderator_message': client.getMessage(87),

            'moderator_message_online': client.getMessage(93),

            'search_message': client.getMessage(95),

            'choose_rieltor': client.getMessage(97),


            'end_text_area': client.getMessage(99),
            'end_text_flat': client.getMessage(100),
            'end_text_land': client.getMessage(101),
            'end_text_free_area': client.getMessage(102),

            'end_text_rieltor_area': client.getMessage(107),
            'end_text_rieltor_flat': client.getMessage(108),
            'end_text_rieltor_land': client.getMessage(109),
            'end_text_rieltor_free_area': client.getMessage(110),

            'area_list': client.getMessage(115),

        }
    else:
        MESSAGES = {
            'start': client.getMessage(33),
            
            'language': client.getMessage(34),

            'area': client.getMessage(35),
            'flat': client.getMessage(36),
            'land': client.getMessage(37),
            'free_area': client.getMessage(38),

            'title_added': client.getMessage(39),

            'region_added': client.getMessage(40),

            'geo1': client.getMessage(41),
            'geo2': client.getMessage(42),
            'geo3': client.getMessage(43),

            'area_started': client.getMessage(44),
            'flat_started': client.getMessage(45),
            'land_started': client.getMessage(46),
            'free_area_started': client.getMessage(47),

            'area_rooms_added': client.getMessage(48),
            'area_square_added': client.getMessage(49),
            
            'flat_rooms_added': client.getMessage(48),
            'flat_square_added': client.getMessage(49),

            'land_square_added': client.getMessage(49),

            'free_area_square_added': client.getMessage(49),
            'free_area_state_added': client.getMessage(46),

            'photo1': client.getMessage(50),
            'photo2': client.getMessage(51),
            'photo3': client.getMessage(52),

            'ammount': client.getMessage(53),
            'ammount_set': client.getMessage(54),

            'contacts': client.getMessage(55),

            'price_list': client.getMessage(56),
            'choose_action': client.getMessage(57),
            'filter': client.getMessage(58),
            'send_text': client.getMessage(59),

            'choose_photo_edit': client.getMessage(60),

            'edit_text_now': client.getMessage(61),

            'data_clear': client.getMessage(62),

            "digits_only": client.getMessage(63),

            "price_list2": client.getMessage(64),

            "filters_clear": client.getMessage(68),
            "prop_state": client.getMessage(69),
            "no_ann": client.getMessage(70),

            "main_floor": client.getMessage(73),
            "floor": client.getMessage(74),

            'area_search': client.getMessage(79),
            'flat_search': client.getMessage(80),
            'land_search': client.getMessage(81),
            'free_area_search': client.getMessage(82),

            'choose_action_after_language': client.getMessage(88),
            'choose_action_rent': client.getMessage(89),
            'choose_action_sale': client.getMessage(90),
            'choose_action_search': client.getMessage(91),

            'moderator_message': client.getMessage(92),

            'moderator_message_online': client.getMessage(94),

            'search_message': client.getMessage(96),

            'choose_rieltor': client.getMessage(98),

            'end_text_area': client.getMessage(103),
            'end_text_flat': client.getMessage(104),
            'end_text_land': client.getMessage(105),
            'end_text_free_area': client.getMessage(106),

            'end_text_rieltor_area': client.getMessage(111),
            'end_text_rieltor_flat': client.getMessage(112),
            'end_text_rieltor_land': client.getMessage(113),
            'end_text_rieltor_free_area': client.getMessage(114),

            'area_list': client.getMessage(116),

        }

    return MESSAGES


