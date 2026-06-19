
USE GestionTramite;

CREATE TABLE TipoEstado (
    codTipoEstado INT AUTO_INCREMENT PRIMARY KEY,
    nombreTipoEstado VARCHAR(100) NOT NULL
);

CREATE TABLE TipoTramite (
    codTipoTramite INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraBajaTT DATETIME,
    nombreTipoTramite VARCHAR(100) NOT NULL,
    cantidadDiasMaximoDocumentacion INT NOT NULL
);

CREATE TABLE EstadoTramite (
    codEstadoTramite INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraBajaEstadoTramite DATETIME,
    nombreEstadoTramite VARCHAR(100) NOT NULL,
    codTipoEstado INT NOT NULL,

    CONSTRAINT estado_tramite_tipo_estado_fk
        FOREIGN KEY (codTipoEstado)
        REFERENCES TipoEstado(codTipoEstado)
);

CREATE TABLE Consultor (
    legajoConsultor INT AUTO_INCREMENT PRIMARY KEY,
    nombreApellidoConsultor VARCHAR(150) NOT NULL,
    fechaHoraBajaConsultor DATETIME
);

CREATE TABLE Cliente (
    dniCliente INT PRIMARY KEY,
    codUsuario INT NOT NULL,
    nombreApellidoCliente VARCHAR(150) NOT NULL,
    fechaHoraBajaCliente DATETIME,
    emailCliente VARCHAR(150) NOT NULL
);

CREATE TABLE Tramite (
    numeroTramite INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraIngresoTramite DATETIME NOT NULL,
    fechaHoraFinReal DATETIME,
    fechaHoraInicioReal DATETIME,
    observacionesTramite VARCHAR(255),
    fechaHoraLimiteTramiteDocumentacion DATETIME,

    codTipoTramite INT NOT NULL,
    codEstadoTramite INT NOT NULL,
    legajoConsultor INT NOT NULL,
    dniCliente INT NOT NULL,

    CONSTRAINT tramite_tipo_tramite_fk
        FOREIGN KEY (codTipoTramite)
        REFERENCES TipoTramite(codTipoTramite),

    CONSTRAINT tramite_estado_tramite_fk
        FOREIGN KEY (codEstadoTramite)
        REFERENCES EstadoTramite(codEstadoTramite),

    CONSTRAINT tramite_consultor_fk
        FOREIGN KEY (legajoConsultor)
        REFERENCES Consultor(legajoConsultor),

    CONSTRAINT tramite_cliente_fk
        FOREIGN KEY (dniCliente)
        REFERENCES Cliente(dniCliente)
);

CREATE TABLE TramiteEstado (
    numeroTramite INT NOT NULL,
    codEstadoTramite INT NOT NULL,
    contadorTramiteEstado INT NOT NULL,
    fechaHoraInicioTramiteEstado DATETIME NOT NULL,
    fechaHoraFinTramiteEstado DATETIME,
    observacionesTramiteEstado VARCHAR(255),

    PRIMARY KEY (numeroTramite, codEstadoTramite, contadorTramiteEstado),

    FOREIGN KEY (numeroTramite)
        REFERENCES Tramite(numeroTramite),

    FOREIGN KEY (codEstadoTramite)
        REFERENCES EstadoTramite(codEstadoTramite)
);

CREATE TABLE ConfiguracionTipoTramite (
    nroConfiguracionTT INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraInicioVigenciaTT DATETIME NOT NULL,
    fechaHoraFinVigenciaTT DATETIME,
    codTipoTramite INT NOT NULL,

    CONSTRAINT configtt_tipo_tramite_fk
        FOREIGN KEY (codEstadoTramite)
        REFERENCES TipoTramite(codTipoTramite)
);

CREATE TABLE ConfiguracionTipoTramiteEstadoTramite (
    nroConfiguracionTT INT NOT NULL,
    codEstadoTramite INT NOT NULL,
    ordenTipoTramiteEstadoTramite INT NOT NULL,

    PRIMARY KEY (nroConfiguracionTT, codEstadoTramite),

    CONSTRAINT config_tt_estado_config_fk
        FOREIGN KEY (nroConfiguracionTT)
        REFERENCES ConfiguracionTipoTramite(nroConfiguracionTT),

    CONSTRAINT config_tt_estado_estado_fk
        FOREIGN KEY (codEstadoTramite)
        REFERENCES EstadoTramite(codEstadoTramite)
);

CREATE TABLE TipoDocumentacion (
    codTipoDocumentacion INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraBajaTipoDocumentacion DATETIME,
    nombreTipoDocumentacion VARCHAR(100) NOT NULL,
    requiereEntregaWeb BOOLEAN NOT NULL
);

CREATE TABLE ConfiguracionDocumentacion (
    nroConfiguracionDocumentacion INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraInicioVigenciaTTTD DATETIME NOT NULL,
    fechaHoraFinVigenciaTTTD DATETIME,
    codTipoTramite INT NOT NULL,

    CONSTRAINT config_doc_tipo_tramite_fk
        FOREIGN KEY (codTipoTramite)
        REFERENCES TipoTramite(codTipoTramite)
);

CREATE TABLE TipoTramiteTipoDocumentacion (
    nroConfiguracionDocumentacion INT NOT NULL,
    codTipoDocumentacion INT NOT NULL,

    PRIMARY KEY (nroConfiguracionDocumentacion, codTipoDocumentacion),

    CONSTRAINT tttd_config_doc_fk
        FOREIGN KEY (nroConfiguracionDocumentacion)
        REFERENCES ConfiguracionDocumentacion(nroConfiguracionDocumentacion),

    CONSTRAINT tttd_tipo_doc_fk
        FOREIGN KEY (codTipoDocumentacion)
        REFERENCES TipoDocumentacion(codTipoDocumentacion)
);

CREATE TABLE DocumentacionTramite (
    numeroTramite INT NOT NULL,
    codTipoDocumentacion INT NOT NULL,
    fechaHoraIngresoDocumentacion DATETIME NOT NULL,
    urlDocumentacion VARCHAR(255) NOT NULL,

    PRIMARY KEY (numeroTramite, codTipoDocumentacion, fechaHoraIngresoDocumentacion),

    CONSTRAINT doc_tramite_tramite_fk
        FOREIGN KEY (numeroTramite)
        REFERENCES Tramite(numeroTramite),

    CONSTRAINT doc_tramite_tipo_doc_fk
        FOREIGN KEY (codTipoDocumentacion)
        REFERENCES TipoDocumentacion(codTipoDocumentacion)
);

CREATE TABLE ConfiguracionAgenda (
    nroConfiguracionAgenda INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraInicioVigenciaAgenda DATETIME NOT NULL,
    fechaHoraFinVigenciaAgenda DATETIME
);

CREATE TABLE ConfigAgendaConsultor (
    nroConfiguracionAgenda INT NOT NULL,
    legajoConsultor INT NOT NULL,
    cantMaximaTramites INT NOT NULL,

    PRIMARY KEY (nroConfiguracionAgenda, legajoConsultor),

    CONSTRAINT config_agenda_consultor_config_fk
        FOREIGN KEY (nroConfiguracionAgenda)
        REFERENCES ConfiguracionAgenda(nroConfiguracionAgenda),

    CONSTRAINT config_agenda_consultor_consultor_fk
        FOREIGN KEY (legajoConsultor)
        REFERENCES Consultor(legajoConsultor)
);

CREATE TABLE ConfiguracionCosto (
    nroConfiguracionCosto INT AUTO_INCREMENT PRIMARY KEY,
    fechaHoraInicioVigenciaCosto DATETIME NOT NULL,
    fechaHoraFinVigenciaCosto DATETIME
);

CREATE TABLE ConfiguracionCostoTT (
    nroConfiguracionCosto INT NOT NULL,
    codTipoTramite INT NOT NULL,
    montoCostoBase DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (nroConfiguracionCosto, codTipoTramite),

    CONSTRAINT config_costo_tt_config_fk
        FOREIGN KEY (nroConfiguracionCosto)
        REFERENCES ConfiguracionCosto(nroConfiguracionCosto),

    CONSTRAINT config_costo_tt_tipo_tramite_fk
        FOREIGN KEY (codTipoTramite)
        REFERENCES TipoTramite(codTipoTramite)
);