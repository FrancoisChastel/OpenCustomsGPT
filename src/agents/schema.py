SAD_ITEM_SCHEMA = f"""
CREATE TABLE sydonia_mg.sydonia_mg.sad_item (
    instanceid bigint,
    key_itm_nbr bigint,
    pck_nbr bigint,
    pck_mrk1 text,
    pck_mrk2 text,
    pck_typ_cod text,
    pck_typ_nam text,
    tar_hsc_nb1 text,
    tar_hsc_nb2 text,
    tar_hsc_nb3 double precision,
    tar_hsc_nb4 text,
    tar_hsc_nb5 text,
    tar_hsc_tsc_dat timestamp without time zone,
    tar_hsc_tsc_sta double precision,
    tar_prf text,
    tar_prc_ext bigint,
    tar_prc_nat bigint,
    tar_quo text,
    tar_pri double precision,
    tar_vmt double precision,
    tar_vdt text,
    tar_att text,
    tar_aic double precision,
    gds_org_cty text,
    gds_org_crg double precision,
    gds_ctn_ct1 double precision,
    gds_ctn_ct2 double precision,
    gds_ctn_ct3 double precision,
    gds_ctn_ct4 double precision,
    gds_dsc text,
    gds_ds3 text,
    lnk_tpt text,
    lnk_tpt_sln double precision,
    lnk_prv_doc text,
    lnk_prv_whs double precision,
    lic_cod text,
    lic_amt_val double precision,
    lic_amt_qty double precision,
    txt_fre text,
    txt_rsv text,
    tax_amt bigint,
    tax_gty double precision,
    tax_mop bigint,
    tax_ctr double precision,
    tax_dty double precision,
    vit_wgt_grs double precision,
    vit_wgt_net double precision,
    vit_cst bigint,
    vit_cif bigint,
    vit_adj double precision,
    vit_stv bigint,
    vit_alp double precision,
    vit_inv_amt_nmu double precision,
    vit_inv_amt_fcx double precision,
    vit_inv_cur_cod text,
    vit_inv_cur_nam text,
    vit_inv_cur_rat double precision,
    vit_inv_cur_ref bigint,
    vit_fob_amt_nmu double precision,
    vit_fob_amt_fcx double precision,
    vit_fob_cur_cod double precision,
    vit_fob_cur_nam double precision,
    vit_fob_cur_rat double precision,
    vit_fob_cur_ref double precision,
    vit_efr_amt_nmu double precision,
    vit_efr_amt_fcx double precision,
    vit_efr_cur_cod text,
    vit_efr_cur_nam text,
    vit_efr_cur_rat double precision,
    vit_efr_cur_ref double precision,
    vit_ifr_amt_nmu double precision,
    vit_ifr_amt_fcx double precision,
    vit_ifr_cur_cod text,
    vit_ifr_cur_nam text,
    vit_ifr_cur_rat double precision,
    vit_ifr_cur_ref double precision,
    vit_ins_amt_nmu double precision,
    vit_ins_amt_fcx double precision,
    vit_ins_cur_cod text,
    vit_ins_cur_nam text,
    vit_ins_cur_rat double precision,
    vit_ins_cur_ref double precision,
    vit_otc_amt_nmu double precision,
    vit_otc_amt_fcx double precision,
    vit_otc_cur_cod text,
    vit_otc_cur_nam text,
    vit_otc_cur_rat double precision,
    vit_otc_cur_ref double precision,
    vit_ded_amt_nmu double precision,
    vit_ded_amt_fcx double precision,
    vit_ded_cur_cod text,
    vit_ded_cur_nam text,
    vit_ded_cur_rat double precision,
    vit_ded_cur_ref double precision,
    vit_mkt_rat double precision,
    vit_mkt_cur double precision,
    vit_mkt_amt double precision,
    vit_mkt_bse_dsc double precision,
    vit_mkt_bse_amt double precision,
    blk_vin double precision,
    blk_srp double precision,
    blk_fob double precision,
    flp1 text,
    quo_id double precision,
    quo_itm_nbr double precision,
    doc_ref_dat timestamp without time zone,
    doc_ref_nbr double precision,
    wri_sup_cod double precision,
    wri_sup_nam double precision,
    wri_sup_qty double precision,
    wri_prg double precision,
    lnk_prv_wde text,
    lnk_prv_doc2 text
);

COMMENT ON COLUMN sydonia_mg.sad_item.instanceid IS 'Internal key';
COMMENT ON COLUMN sydonia_mg.sad_item.key_itm_nbr IS 'Item Number';
COMMENT ON COLUMN sydonia_mg.sad_item.pck_nbr IS 'Number of packages - item';
COMMENT ON COLUMN sydonia_mg.sad_item.pck_mrk1 IS 'Marks of Packages 1';
COMMENT ON COLUMN sydonia_mg.sad_item.pck_mrk2 IS 'Marks of Packages 2';
COMMENT ON COLUMN sydonia_mg.sad_item.pck_typ_cod IS 'Kind of packages - code';
COMMENT ON COLUMN sydonia_mg.sad_item.pck_typ_nam IS 'Kind of packages - name';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_nb1 IS 'Harmonized system commodity code';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_nb2 IS 'Commodity code (national precision 2)';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_nb3 IS 'Commodity code (national precision 3)';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_nb4 IS 'Commodity code (national precision 4)';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_nb5 IS 'Commodity code (national precision 5)';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_tsc_dat IS 'Value details - item';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_hsc_tsc_sta IS 'Attached documents codes - item';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_prf IS 'Preference code';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_prc_ext IS 'Extended customs procedure code';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_prc_nat IS 'National customs procedure code';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_quo IS 'Quota reference';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_pri IS 'Item price';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_vmt IS 'Valuation Method';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_vdt IS 'Value details - item';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_att IS 'Attached documents codes - item';
COMMENT ON COLUMN sydonia_mg.sad_item.tar_aic IS 'A.I. code';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_org_cty IS 'Country of origin - code';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_org_crg IS 'Country of origin - region code';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_ctn_ct1 IS 'Container Number 1';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_ctn_ct2 IS 'Container Number 2';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_ctn_ct3 IS 'Container Number 3';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_ctn_ct4 IS 'Container Number 4';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_dsc IS 'Description of goods';
COMMENT ON COLUMN sydonia_mg.sad_item.gds_ds3 IS 'Commercial Description of goods';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_tpt IS 'Summary declaration (Transport document number)';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_tpt_sln IS 'Previous document reference';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_prv_doc IS 'Previous document reference';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_prv_whs IS 'Additional warehouse code';
COMMENT ON COLUMN sydonia_mg.sad_item.lic_cod IS 'Licence reference number';
COMMENT ON COLUMN sydonia_mg.sad_item.lic_amt_val IS 'Value amount deducted from licence';
COMMENT ON COLUMN sydonia_mg.sad_item.lic_amt_qty IS 'Quantity deducted from licence';
COMMENT ON COLUMN sydonia_mg.sad_item.txt_fre IS 'Reserved field (use not defined)';
COMMENT ON COLUMN sydonia_mg.sad_item.txt_rsv IS 'Free text';
COMMENT ON COLUMN sydonia_mg.sad_item.tax_amt IS 'Item amount of Duties and taxes';
COMMENT ON COLUMN sydonia_mg.sad_item.tax_gty IS 'Item guaranted amount of Duties and taxes';
COMMENT ON COLUMN sydonia_mg.sad_item.tax_mop IS 'Mode of payment for item amount';
COMMENT ON COLUMN sydonia_mg.sad_item.tax_ctr IS 'Counter of normal Mode of payments';
COMMENT ON COLUMN sydonia_mg.sad_item.tax_dty IS 'Displayed item amount of Duties and taxes';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_wgt_grs IS 'Gross mass';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_wgt_net IS 'Net mass';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_cst IS 'Amount of added costs in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_cif IS 'CIF amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_adj IS 'Rate of adjustment';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_stv IS 'Statistical value';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_alp IS 'Alpha coefficient of apportionment';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_amt_nmu IS 'Amount of the invoice in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_amt_fcx IS 'Amount of the invoice in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_cur_cod IS 'Currency code for the invoice';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_cur_nam IS 'Currency name for the invoice';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_cur_rat IS 'Currency rate for the invoice';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_inv_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_amt_nmu IS 'FOB amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_amt_fcx IS 'FOB amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_cur_cod IS 'Currency code for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_cur_nam IS 'Currency name for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_cur_rat IS 'Currency rate for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_fob_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_amt_nmu IS 'External freight amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_amt_fcx IS 'External freight amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_cur_cod IS 'Currency code for the external freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_cur_nam IS 'Currency name for the external freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_cur_rat IS 'Currency rate for the external freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_efr_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_amt_nmu IS 'Internal freight amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_amt_fcx IS 'Internal freight amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_cur_cod IS 'Currency code for the internal freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_cur_nam IS 'Currency name for the internal freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_cur_rat IS 'Currency rate for the internal freight';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ifr_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_amt_nmu IS 'Insurance amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_amt_fcx IS 'Insurance amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_cur_cod IS 'Currency code for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_cur_nam IS 'Currency name for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_cur_rat IS 'Currency rate for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ins_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_amt_nmu IS 'Other costs amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_amt_fcx IS 'Other costs amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_cur_cod IS 'Currency code for the other costs';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_cur_nam IS 'Currency name for the other costs';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_cur_rat IS 'Currency rate for the other costs';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_otc_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_amt_nmu IS 'Deductions amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_amt_fcx IS 'Deductions amount in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_cur_cod IS 'Currency code for the deductions';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_cur_nam IS 'Currency name for the deductions';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_cur_rat IS 'Currency rate for the deductions';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_ded_cur_ref IS 'Rate reference unit';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_mkt_rat IS 'Market value rate';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_mkt_cur IS 'National currency code';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_mkt_amt IS 'Market value amount';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_mkt_bse_dsc IS 'Market value basis description';
COMMENT ON COLUMN sydonia_mg.sad_item.vit_mkt_bse_amt IS 'Market value basis amount';
COMMENT ON COLUMN sydonia_mg.sad_item.blk_vin IS 'Block VIN';
COMMENT ON COLUMN sydonia_mg.sad_item.blk_srp IS 'Block SRP';
COMMENT ON COLUMN sydonia_mg.sad_item.blk_fob IS 'Block FOB';
COMMENT ON COLUMN sydonia_mg.sad_item.flp1 IS 'Flip';
COMMENT ON COLUMN sydonia_mg.sad_item.quo_id IS 'Quotation ID';
COMMENT ON COLUMN sydonia_mg.sad_item.quo_itm_nbr IS 'Quotation item number';
COMMENT ON COLUMN sydonia_mg.sad_item.doc_ref_dat IS 'Document reference date';
COMMENT ON COLUMN sydonia_mg.sad_item.doc_ref_nbr IS 'Document reference number';
COMMENT ON COLUMN sydonia_mg.sad_item.wri_sup_cod IS 'Supplier code for write-off';
COMMENT ON COLUMN sydonia_mg.sad_item.wri_sup_nam IS 'Supplier name for write-off';
COMMENT ON COLUMN sydonia_mg.sad_item.wri_sup_qty IS 'Supplier quantity for write-off';
COMMENT ON COLUMN sydonia_mg.sad_item.wri_prg IS 'Write-off program';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_prv_wde IS 'Previous WDE linkage';
COMMENT ON COLUMN sydonia_mg.sad_item.lnk_prv_doc2 IS 'Previous document reference 2';
"""

SAD_GEN_SCHEMA = f"""
CREATE TABLE sydonia_mg.sad_gen (
    instanceid bigint,
    rls_cuo_cod double precision,
    rls_cuo_nam double precision,
    rls_ref double precision,
    rls_inf double precision,
    rls_dat timestamp without time zone,
    rls_tim double precision,
    prv_dty double precision,
    pty_col_dsc text,
    pty_col_ind double precision,
    pty_blu double precision,
    pty_red double precision,
    pty_yel double precision,
    pty_gre double precision,
    pty_oas double precision,
    pty_que double precision,
    pty_wde text,
    pty_frm_nbr double precision,
    pty_frm_tot bigint,
    pty_nbr_ldl double precision,
    pty_nbr_itm bigint,
    pty_nbr_pck bigint,
    pty_plc double precision,
    pty_cde double precision,
    ide_cuo_cod text,
    ide_cuo_nam text,
    ide_typ_sad text,
    ide_typ_prc bigint,
    ide_typ_typ text,
    ide_typ_trs double precision,
    ide_man text,
    ide_bar text,
    ide_reg_ser text,
    ide_reg_nbr bigint,
    ide_reg_dat timestamp without time zone,
    ide_ast_ser text,
    ide_ast_nbr double precision,
    ide_ast_dat timestamp without time zone,
    ide_rcp_ser text,
    ide_rcp_nbr double precision,
    ide_rcp_dat timestamp without time zone,
    ide_rcp_typ double precision,
    ide_rcp_cuo text,
    ide_pst_nbr double precision,
    ide_pst_dat timestamp without time zone,
    ide_pst_tmp_pre double precision,
    ide_pst_tmp_ty1 text,
    ide_pst_tmp_ty2 text,
    cmp_con_cod text,
    dec_flg double precision,
    dec_cod text,
    dec_ref_yer bigint,
    dec_ref_nbr text,
    gen_cty_flt text,
    gen_cty_trd text,
    gen_cty_ept_cod text,
    gen_cty_ept_nam text,
    gen_cty_ept_crg double precision,
    gen_cty_des_cod text,
    gen_cty_des_nam text,
    gen_cty_des_crg double precision,
    gen_cty_org text,
    gen_vdt bigint,
    gen_cap double precision,
    gen_fre text,
    tpt_mot_dpa_cty text,
    tpt_mot_brd_nam text,
    tpt_mot_brd_cty text,
    tpt_mot_brd_cod bigint,
    tpt_mot_inl double precision,
    tpt_ctf bigint,
    tpt_tod_cod text,
    tpt_tod_plc text,
    tpt_tod_sit double precision,
    tpt_cuo_cod text,
    tpt_cuo_nam text,
    tpt_lop_cod text,
    tpt_lop_nam text,
    tpt_lop_cty text,
    tpt_loc text,
    tpt_t1 double precision,
    fin_tra_na1 double precision,
    fin_tra_na2 double precision,
    fin_bnk_cod double precision,
    fin_bnk_nam text,
    fin_bnk_bra double precision,
    fin_bnk_fre text,
    fin_top_cod text,
    fin_top_nam text,
    fin_acc text,
    fin_pin double precision,
    fin_mpn text,
    fin_amt_mnl double precision,
    fin_amt_fee bigint,
    fin_amt_dty bigint,
    fin_amt_tbp bigint,
    fin_gty_nam text,
    fin_gty_amt bigint,
    fin_gty_dat timestamp without time zone,
    fin_gty_cty_cod double precision,
    fin_gty_cty_nam double precision,
    vgs_wrk bigint,
    vgs_wgt_grs double precision,
    vgs_cst bigint,
    vgs_cif bigint,
    vgs_tot_nmu bigint,
    vgs_tot_fcx double precision,
    vgs_tot_grs double precision,
    vgs_inv_amt_nmu double precision,
    vgs_inv_amt_fcx double precision,
    vgs_inv_cur_cod text,
    vgs_inv_cur_nam text,
    vgs_inv_cur_rat double precision,
    vgs_inv_cur_ref bigint,
    vgs_fob_amt_nmu double precision,
    vgs_fob_amt_fcx double precision,
    vgs_fob_cur_cod double precision,
    vgs_fob_cur_nam double precision,
    vgs_fob_cur_rat double precision,
    vgs_fob_cur_ref double precision,
    vgs_efr_amt_nmu double precision,
    vgs_efr_amt_fcx double precision,
    vgs_efr_cur_cod text,
    vgs_efr_cur_nam text,
    vgs_efr_cur_rat double precision,
    vgs_efr_cur_ref double precision,
    vgs_ifr_amt_nmu double precision,
    vgs_ifr_amt_fcx double precision,
    vgs_ifr_cur_cod text,
    vgs_ifr_cur_nam text,
    vgs_ifr_cur_rat double precision,
    vgs_ifr_cur_ref double precision,
    vgs_ins_amt_nmu double precision,
    vgs_ins_amt_fcx double precision,
    vgs_ins_cur_cod text,
    vgs_ins_cur_nam text,
    vgs_ins_cur_rat double precision,
    vgs_ins_cur_ref double precision,
    vgs_otc_amt_nmu double precision,
    vgs_otc_amt_fcx double precision,
    vgs_otc_cur_cod text,
    vgs_otc_cur_nam text,
    vgs_otc_cur_rat double precision,
    vgs_otc_cur_ref double precision,
    vgs_ded_amt_nmu double precision,
    vgs_ded_amt_fcx double precision,
    vgs_ded_cur_cod text,
    vgs_ded_cur_nam text,
    vgs_ded_cur_rat double precision,
    vgs_ded_cur_ref double precision,
    whs_cod text,
    whs_tim double precision,
    trs_rsp_cod text,
    trs_sgt_plc text,
    trs_sgt_dat timestamp without time zone,
    trs_des_cuo text,
    trs_des_cod text,
    trs_des_cty text,
    trs_sls_nbr double precision,
    trs_sls_ide double precision,
    trs_ctl double precision,
    trs_lim double precision,
    trs_cof double precision,
    ast_ryr bigint,
    ast_ayr bigint,
    ast_tot bigint,
    ast_amt double precision,
    ast_stn double precision,
    ast_std double precision,
    ast_sts double precision,
    rlo_nbr double precision,
    exa_sec text,
    exa_wgt double precision,
    lst_rcp_amt double precision,
    lst_rcp_ser double precision,
    lst_rcp_nbr double precision,
    lst_rcp_dat timestamp without time zone,
    lst_rcp_typ double precision,
    lst_rcp_cuo double precision,
    broker_stamp double precision,
    customs_stamp double precision,
    doc_ref_dat timestamp without time zone,
    doc_ref_nbr double precision,
    tna_flg text,
    tna_mtf text,
    vgs_inv_amt_fci double precision,
    ide_sim double precision,
    grp_nbri double precision,
    grp_nbrr double precision,
    step bigint,
    ide_can_dat timestamp without time zone,
    exi_nbr double precision,
    t1_nbr double precision,
    lck_flg text,
    pty_ver bigint,
    scn_ext text,
    cup_sel text,
    cup_itm text,
    cup_rgsr text
);

-------------------------------------------------------------------------------
COMMENT ON COLUMN sydonia_mg.sad_gen.instanceid IS 'Internal key';
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_cuo_cod IS 'Export Release Customs Office Code';
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_cuo_nam IS 'Export Release Customs Office Name';
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_ref IS 'Export Release Reference';
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_inf IS 'Export Release Information';
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_dat IS 'Export Release date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.rls_tim IS 'Export Release Time';
COMMENT ON COLUMN sydonia_mg.sad_gen.prv_dty IS 'Previous amount of duties & taxes for declaration';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_col_dsc IS 'Selected colour description';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_col_ind IS 'Selected colour indicator';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_blu IS 'Blue flag - medium level of risk';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_red IS 'Red flag - high level of risk';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_yel IS 'Yellow flag - low level of risk';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_gre IS 'Green flag - no risk at all';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_oas IS 'Selected other administrations lock';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_que IS 'Query flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_wde IS 'Working date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_frm_nbr IS 'Number of the Form';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_frm_tot IS 'Total number of Forms';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_nbr_ldl IS 'Number of loading lists';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_nbr_itm IS 'Number of items';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_nbr_pck IS 'Total number of packages';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_plc IS 'Place of declaration';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_cde IS 'Date of declaration';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_cuo_cod IS 'Office Code';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_cuo_nam IS 'Office Name';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_typ_sad IS 'Model of Declaration';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_typ_prc IS 'General Regime';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_typ_typ IS 'Declaration type (I, E)';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_typ_trs IS 'Type of Transit document code';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_man IS 'Manifest reference number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_bar IS 'Declaration Barcode';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_reg_ser IS 'Registration serial';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_reg_nbr IS 'Registration number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_reg_dat IS 'Registration date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_ast_ser IS 'Assessment Serial';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_ast_nbr IS 'Assessment Number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_ast_dat IS 'Assessment date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_rcp_ser IS 'Receipt Serial';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_rcp_nbr IS 'Receipt Number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_rcp_dat IS 'Receipt date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_rcp_typ IS 'Receipt type';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_rcp_cuo IS 'Receipt Office';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_pst_nbr IS 'Receipt - number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_pst_dat IS 'Post-entry - date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_pst_tmp_pre IS 'Last prepayment account';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_pst_tmp_ty1 IS 'Last prepayment account';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_pst_tmp_ty2 IS 'Last prepayment account';
COMMENT ON COLUMN sydonia_mg.sad_gen.cmp_con_cod IS 'Consignee - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.dec_flg IS 'Declarant - flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.dec_cod IS 'Declarant Code';
COMMENT ON COLUMN sydonia_mg.sad_gen.dec_ref_yer IS 'Declarant reference Year';
COMMENT ON COLUMN sydonia_mg.sad_gen.dec_ref_nbr IS 'Declarant reference number';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_flt IS 'Country of first destination / last provenance';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_trd IS 'Trading country';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_ept_cod IS 'Country of export - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_ept_nam IS 'Country of export - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_ept_crg IS 'Country of export - region code';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_des_cod IS 'Country of destination - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_des_nam IS 'Country of destination - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_des_crg IS 'Country of destination - region code';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cty_org IS 'Country of origin - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_vdt IS 'Value details';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_cap IS 'Common Agricultural Policy reference';
COMMENT ON COLUMN sydonia_mg.sad_gen.gen_fre IS 'Comments';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_mot_dpa_cty IS 'Nat. of Means of Transport at depart./arrival';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_mot_brd_nam IS 'Identity of Means of Transport at the border';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_mot_brd_cty IS 'Nationality of Means of Transport at the border';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_mot_brd_cod IS 'Mode of transport crossing the border';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_mot_inl IS 'Inland mode of transport';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_ctf IS 'Container flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_tod_cod IS 'Incoterm, code';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_tod_plc IS 'Incoterm, place';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_tod_sit IS 'Delivery terms - situation code';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_cuo_cod IS 'Border customs office - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_cuo_nam IS 'Border customs office - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_lop_cod IS 'Place of loading/unloading - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_lop_nam IS 'Place of loading/unloading - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_lop_cty IS 'Place of loading/unloading - country code';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_loc IS 'Location of goods';
COMMENT ON COLUMN sydonia_mg.sad_gen.tpt_t1 IS 'Reference to T1 (instance id)';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_tra_na1 IS 'Nature of transaction - code 1';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_tra_na2 IS 'Nature of transaction - code 2';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_bnk_cod IS 'Bank - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_bnk_nam IS 'Bank - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_bnk_bra IS 'Bank branch - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_bnk_fre IS 'Bank file number';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_top_cod IS 'Terms of payment - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_top_nam IS 'Terms of payment - description';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_acc IS 'Accounting Code';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_pin IS 'PIN';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_mpn IS 'Mode of Payment';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_amt_mnl IS 'Total taxes amount by manual input';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_amt_fee IS 'Total Global Taxes';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_amt_dty IS 'Total General';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_amt_tbp IS 'Amount for the Situation of payment';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_gty_nam IS 'Guarantee reference code';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_gty_amt IS 'Guarantee - amount';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_gty_dat IS 'Guarantee - date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_gty_cty_cod IS 'Country code excluded from guarantee';
COMMENT ON COLUMN sydonia_mg.sad_gen.fin_gty_cty_nam IS 'Country name excluded from guarantee';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_wrk IS 'Calculation working mode';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_wgt_grs IS 'Gross mass';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_cst IS 'Total amount of added costs in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_cif IS 'Total CIF amount in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_tot_nmu IS 'Total items in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_tot_fcx IS 'Total items in foreign currency invoice value';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_tot_grs IS 'Total items, gross mass amount';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_amt_nmu IS 'Amount of the invoice in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_amt_fcx IS 'Amount of the invoice in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_cur_cod IS 'Currrency code for the invoice';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_cur_nam IS 'Invoice currency - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_cur_rat IS 'Currency rate for the invoice';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_cur_ref IS 'Rate ref unit';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_amt_nmu IS 'Amount of the FOB in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_amt_fcx IS 'Amount of the FOB in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_cur_cod IS 'Currency code for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_cur_nam IS 'Currency name for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_cur_rat IS 'Exchange rate for the FOB';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_fob_cur_ref IS 'Rate ref unit';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_amt_nmu IS 'Amount of the insurance in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_amt_fcx IS 'Amount of the insurance in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_cur_cod IS 'Currency code for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_cur_nam IS 'Currency name for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_cur_rat IS 'Exchange rate for the insurance';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ins_cur_ref IS 'Rate ref unit';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_amt_nmu IS 'Amount of other costs in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_amt_fcx IS 'Amount of other costs in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_cur_cod IS 'Currency code for other costs';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_cur_nam IS 'Currency name for other costs';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_cur_rat IS 'Exchange rate for other costs';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_otc_cur_ref IS 'Rate ref unit';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_amt_nmu IS 'Amount of deductions in national monetary units';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_amt_fcx IS 'Amount of deductions in foreign currency';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_cur_cod IS 'Currency code for deductions';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_cur_nam IS 'Currency name for deductions';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_cur_rat IS 'Exchange rate for deductions';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_ded_cur_ref IS 'Rate ref unit';
COMMENT ON COLUMN sydonia_mg.sad_gen.whs_cod IS 'Identification of warehouse';
COMMENT ON COLUMN sydonia_mg.sad_gen.whs_tim IS 'Warehouse time delay';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_rsp_cod IS 'Principal responsible for transit - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_sgt_plc IS 'Place of signature of transit';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_sgt_dat IS 'Date of signature of transit';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_des_cuo IS 'Customs office of destination for transit - name';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_des_cod IS 'Customs office of destination for transit - code';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_des_cty IS 'Country of customs office of destination for transit';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_sls_nbr IS 'Seals affixed - Number';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_sls_ide IS 'Seals affixed - Identity';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_ctl IS 'Results of control';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_lim IS 'Transit time limit (date)';
COMMENT ON COLUMN sydonia_mg.sad_gen.trs_cof IS 'Customs officer name';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_ryr IS 'Registration Year';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_ayr IS 'Assessment Year';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_tot IS 'Total Items Taxes';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_amt IS 'Total amount assessed for declaration';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_stn IS 'Statement Number';
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_std IS 'Statement date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.ast_sts IS 'Statement Serial';
COMMENT ON COLUMN sydonia_mg.sad_gen.rlo_nbr IS 'Release Order Sequential Number';
COMMENT ON COLUMN sydonia_mg.sad_gen.exa_sec IS 'Declaration Assigned Section';
COMMENT ON COLUMN sydonia_mg.sad_gen.exa_wgt IS 'Declaration Assigned Weight';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_amt IS 'Total Amount of Last Receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_ser IS 'Receipt serial of last receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_nbr IS 'Number of last receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_dat IS 'Date of last receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_typ IS 'Type of last receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.lst_rcp_cuo IS 'Customs office code of last receipt';
COMMENT ON COLUMN sydonia_mg.sad_gen.broker_stamp IS 'Broker stamp';
COMMENT ON COLUMN sydonia_mg.sad_gen.customs_stamp IS 'Customs stamp';
COMMENT ON COLUMN sydonia_mg.sad_gen.doc_ref_dat IS 'Document reference date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.doc_ref_nbr IS 'Document reference number';
COMMENT ON COLUMN sydonia_mg.sad_gen.tna_flg IS 'Transit flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.tna_mtf IS 'Movement type flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.vgs_inv_amt_fci IS 'Invoice amount in foreign currency (internal)';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_sim IS 'SIM code';
COMMENT ON COLUMN sydonia_mg.sad_gen.grp_nbri IS 'Internal group number';
COMMENT ON COLUMN sydonia_mg.sad_gen.grp_nbrr IS 'External group number';
COMMENT ON COLUMN sydonia_mg.sad_gen.step IS 'Processing step';
COMMENT ON COLUMN sydonia_mg.sad_gen.ide_can_dat IS 'Cancellation date with format YYYY-MM-DD"T"HH24:MI:SS.USZ';;
COMMENT ON COLUMN sydonia_mg.sad_gen.exi_nbr IS 'Exit note number';
COMMENT ON COLUMN sydonia_mg.sad_gen.t1_nbr IS 'T1 number';
COMMENT ON COLUMN sydonia_mg.sad_gen.lck_flg IS 'Lock flag';
COMMENT ON COLUMN sydonia_mg.sad_gen.pty_ver IS 'Version of party data';
COMMENT ON COLUMN sydonia_mg.sad_gen.scn_ext IS 'Screen extension';
COMMENT ON COLUMN sydonia_mg.sad_gen.cup_sel IS 'Selected customs procedure';
COMMENT ON COLUMN sydonia_mg.sad_gen.cup_itm IS 'Customs procedure item';
COMMENT ON COLUMN sydonia_mg.sad_gen.cup_rgsr IS 'Customs procedure registration serial';
"""